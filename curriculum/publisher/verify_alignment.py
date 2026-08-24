"""Verification script to compare model counts and PK alignment between local and target databases."""

import sys
from django.apps import apps
from curriculum.publisher.connection import PublishConnection
from curriculum.publisher.constants import SYNCED_MODEL_NAMES


def verify_alignment(source_db: str = 'default', target_db: str = 'publish_target') -> dict:
    """Compares counts and primary keys between source and target databases."""
    connection = PublishConnection()
    results = {}

    with connection:
        print(f"\n{'='*70}")
        print(f"DATABASE ALIGNMENT VERIFICATION")
        print(f"Source: {connection.get_source_display()}")
        print(f"Target: {connection.get_target_display()}")
        print(f"{'='*70}\n")
        print(f"{'Model':<26} {'Source':>8} {'Target':>8} {'Overlap PKs':>12} {'Status':>14}")
        print(f"{'-'*26} {'-'*8} {'-'*8} {'-'*12} {'-'*14}")

        for model_name in SYNCED_MODEL_NAMES:
            try:
                Model = apps.get_model('curriculum', model_name)
                source_pks = set(Model.objects.using(source_db).values_list('pk', flat=True))
                target_pks = set(Model.objects.using(target_db).values_list('pk', flat=True))

                overlap = len(source_pks.intersection(target_pks))
                source_count = len(source_pks)
                target_count = len(target_pks)

                if target_count == 0:
                    status = "EMPTY TARGET"
                elif source_count == target_count and overlap == source_count:
                    status = "IDENTICAL"
                elif overlap > 0:
                    status = "PARTIAL"
                else:
                    status = "DIVERGED"

                results[model_name] = {
                    'source_count': source_count,
                    'target_count': target_count,
                    'overlap_pks': overlap,
                    'status': status,
                }

                print(f"{model_name:<26} {source_count:>8} {target_count:>8} {overlap:>12} {status:>14}")

            except Exception as e:
                results[model_name] = {'error': str(e)}
                print(f"{model_name:<26} ERROR: {e}")

        print(f"{'='*70}\n")

    return results


if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
    django.setup()
    verify_alignment()
