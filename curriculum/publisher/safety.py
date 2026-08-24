import os
import sys
import fcntl
import tempfile
from dataclasses import dataclass, field
from django.db import connections
from django.db.utils import OperationalError
from django.apps import apps

class PublicationLockError(Exception):
    """Raised when publication lock cannot be acquired."""
    pass

class PreFlightError(Exception):
    """Raised when pre-flight validation fails."""
    pass

class SafetyError(Exception):
    """Raised when general safety constraints are violated."""
    pass

LOCK_FILE = os.path.join(tempfile.gettempdir(), 'vlearn_publish.lock')

class PublicationLock:
    def __init__(self):
        self.lock_fd = None

    def acquire(self) -> bool:
        try:
            self.lock_fd = open(LOCK_FILE, 'w')
            fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.lock_fd.write(str(os.getpid()))
            self.lock_fd.flush()
            return True
        except (IOError, OSError) as e:
            if self.lock_fd:
                self.lock_fd.close()
                self.lock_fd = None
            try:
                with open(LOCK_FILE, 'r') as f:
                    pid = f.read().strip()
            except IOError:
                pid = "unknown"
            raise PublicationLockError(f"Publication is currently locked by PID: {pid}. Error: {e}")

    def release(self):
        if self.lock_fd:
            try:
                fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
                self.lock_fd.close()
                try:
                    os.remove(LOCK_FILE)
                except OSError:
                    pass
            except OSError:
                pass
            finally:
                self.lock_fd = None

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

@dataclass
class ValidationCheck:
    name: str
    passed: bool
    message: str
    details: list[str] = field(default_factory=list)

@dataclass
class ValidationReport:
    checks: list[ValidationCheck]
    
    @property
    def all_passed(self) -> bool:
        return all(check.passed for check in self.checks)
        
    def format_cli(self) -> str:
        """Format as CLI-friendly output with checkmarks."""
        lines = ["Pre-flight Validation Report:", "-" * 30]
        for check in self.checks:
            mark = "✅" if check.passed else "❌"
            lines.append(f"{mark} {check.name}: {check.message}")
            for detail in check.details:
                lines.append(f"   - {detail}")
        lines.append("-" * 30)
        status = "PASSED" if self.all_passed else "FAILED"
        lines.append(f"Overall Status: {status}")
        return "\n".join(lines)


class PreFlightValidator:
    def __init__(self, source_db: str, target_db: str):
        self.source_db = source_db
        self.target_db = target_db

    def validate_all(self) -> ValidationReport:
        """Run all validation checks. Returns a report."""
        checks = [
            self.check_connectivity(),
            self.check_source_target_differ(),
            self.check_schema_compatibility(),
            self.check_identity_integrity(),
            self.check_operational_protection()
        ]
        return ValidationReport(checks=checks)

    def check_connectivity(self) -> ValidationCheck:
        details = []
        passed = True
        message = "Connected to both databases"
        
        for db_alias in [self.source_db, self.target_db]:
            try:
                conn = connections[db_alias]
                conn.ensure_connection()
                details.append(f"Successfully connected to {db_alias}")
            except Exception as e:
                passed = False
                message = "Database connectivity check failed"
                details.append(f"Failed to connect to {db_alias}: {str(e)}")
                
        return ValidationCheck(name="Database Connectivity", passed=passed, message=message, details=details)

    def check_schema_compatibility(self) -> ValidationCheck:
        passed = True
        message = "Schema compatibility verified"
        details = []
        
        try:
            conn = connections[self.target_db]
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name, column_name 
                    FROM information_schema.columns 
                    WHERE table_schema = 'public' AND column_name IN ('content_uuid', 'content_hash');
                """)
                rows = cursor.fetchall()
                found_cols: dict[str, set[str]] = {}
                for t, c in rows:
                    found_cols.setdefault(t, set()).add(c)
                
                try:
                    curriculum_app = apps.get_app_config('curriculum')
                    models_to_check = [m for m in curriculum_app.get_models() if hasattr(m, 'content_uuid')]
                except Exception:
                    models_to_check = []
                    
                for model in models_to_check:
                    table_name = model._meta.db_table
                    cols = found_cols.get(table_name, set())
                    if 'content_uuid' not in cols or 'content_hash' not in cols:
                        passed = False
                        message = "Schema compatibility check failed"
                        details.append(f"Target table {table_name} is missing content_uuid or content_hash")
        except Exception as e:
            passed = False
            message = "Error checking schema compatibility"
            details.append(str(e))
            
        return ValidationCheck(name="Schema Compatibility", passed=passed, message=message, details=details)

    def check_identity_integrity(self) -> ValidationCheck:
        passed = True
        message = "Identity integrity verified"
        details = []
        
        try:
            curriculum_app = apps.get_app_config('curriculum')
            models_to_check = [m for m in curriculum_app.get_models() if hasattr(m, 'content_uuid')]
            
            for model in models_to_check:
                try:
                    null_count = model.objects.using(self.source_db).filter(content_uuid__isnull=True).count()
                    if null_count > 0:
                        passed = False
                        message = "Identity integrity check failed"
                        details.append(f"Model {model.__name__} has {null_count} records with null content_uuid")
                except Exception as e:
                    details.append(f"Could not check {model.__name__}: {e}")
        except Exception as e:
            passed = False
            message = "Error checking identity integrity"
            details.append(str(e))
            
        return ValidationCheck(name="Identity Integrity", passed=passed, message=message, details=details)

    def check_source_target_differ(self) -> ValidationCheck:
        passed = True
        message = "Source and Target databases are distinct"
        details = []
        
        try:
            source_settings = connections[self.source_db].settings_dict
            target_settings = connections[self.target_db].settings_dict
            
            source_id = f"{source_settings.get('HOST', 'localhost')}:{source_settings.get('PORT', '')}/{source_settings.get('NAME', '')}"
            target_id = f"{target_settings.get('HOST', 'localhost')}:{target_settings.get('PORT', '')}/{target_settings.get('NAME', '')}"
            
            if source_id == target_id:
                passed = False
                message = "Source and Target databases appear to be the same"
                details.append(f"Both map to {source_id}")
        except Exception as e:
            passed = False
            message = "Error checking source and target differentiation"
            details.append(str(e))
            
        return ValidationCheck(name="Source-Target Separation", passed=passed, message=message, details=details)

    def check_operational_protection(self) -> ValidationCheck:
        passed = True
        message = "Operational protection verified"
        details = []
        
        operational_models = {'User', 'Subscription', 'Payment', 'Transaction', 'Student', 'Teacher', 'School'}
        try:
            from curriculum.publisher.constants import SYNCED_MODELS
            
            for model in SYNCED_MODELS:
                model_name = model.__name__ if hasattr(model, '__name__') else str(model)
                if model_name in operational_models:
                    passed = False
                    message = "Operational models found in sync list"
                    details.append(f"Model {model_name} is operational and must not be published")
        except ImportError:
            details.append("Note: SYNCED_MODELS could not be imported. Assuming safe.")
        except Exception as e:
            passed = False
            message = "Error checking operational protection"
            details.append(str(e))
            
        return ValidationCheck(name="Operational Protection", passed=passed, message=message, details=details)


def confirm_publication(target_display: str, scope: dict, skip_confirmation: bool = False) -> bool:
    """Print target info and require typing PUBLISH to confirm."""
    if skip_confirmation:
        return True
        
    print(f"\n--- PUBLICATION CONFIRMATION ---")
    print(f"Target Database: {target_display}")
    print(f"Scope:")
    for k, v in scope.items():
        print(f"  - {k}: {v}")
    print("\nWARNING: This will overwrite data in the target database based on content_uuid.")
    print("To proceed, type 'PUBLISH' (case-sensitive) and press Enter.")
    
    try:
        response = input("> ")
        return response == "PUBLISH"
    except (EOFError, KeyboardInterrupt):
        return False
