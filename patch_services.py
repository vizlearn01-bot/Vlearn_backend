import re

with open("organizations/services.py", "r") as f:
    content = f.read()

# Add imports for new models
new_imports = "    TeacherSpecialty,\n    Term,\n    ExamConfiguration,\n"
content = re.sub(r'(SchoolInvitation,\n)', r'\1' + new_imports, content)

new_services = """

class BulkUploadService:
    \"\"\"Handles parsing and importing CSV/Excel files for teacher and student bulk uploads.\"\"\"

    @staticmethod
    def parse_file(file):
        \"\"\"Parse an uploaded CSV or Excel file into a list of dicts.\"\"\"
        import openpyxl
        import csv
        import io
        
        filename = file.name.lower()
        rows = []
        
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            wb = openpyxl.load_workbook(file, read_only=True)
            ws = wb.active
            headers = None
            for i, row in enumerate(ws.iter_rows(values_only=True)):
                if i == 0:
                    headers = [str(h).strip().lower().replace(' ', '_') if h else f'col_{j}' for j, h in enumerate(row)]
                    continue
                if all(cell is None for cell in row):
                    continue
                rows.append(dict(zip(headers, [str(v).strip() if v else '' for v in row])))
            wb.close()
        elif filename.endswith('.csv'):
            content = file.read().decode('utf-8-sig')
            reader = csv.DictReader(io.StringIO(content))
            for row in reader:
                rows.append({k.strip().lower().replace(' ', '_'): v.strip() for k, v in row.items()})
        else:
            raise ValidationError("Unsupported file format. Please upload a CSV or Excel (.xlsx) file.")
        
        return rows

    @staticmethod
    def import_teachers(school, rows):
        \"\"\"Import teachers from parsed rows. Returns (created_count, errors).\"\"\"
        from Resources.models import User, UserProfile
        
        created = []
        errors = []
        
        for i, row in enumerate(rows, start=2):  # start=2 because row 1 is headers
            name = row.get('teacher_name', '') or row.get('name', '')
            phone = row.get('phone_number', '') or row.get('phone', '')
            email = row.get('email', '')
            tsc = row.get('tsc_number', '') or row.get('tsc', '')
            specialties_str = row.get('subject_specialties', '') or row.get('specialties', '')
            
            if not name:
                errors.append({'row': i, 'error': 'Teacher name is required'})
                continue
            if not phone:
                errors.append({'row': i, 'error': 'Phone number is required'})
                continue
            
            # Check for duplicate phone
            if User.objects.filter(phone_number=phone).exists():
                existing_user = User.objects.get(phone_number=phone)
                # Check if already a member of this school
                if OrganizationMembership.objects.filter(user=existing_user, school=school).exists():
                    errors.append({'row': i, 'error': f'Teacher with phone {phone} already exists in this school'})
                    continue
                # Add to school as existing user
                OrganizationMembership.objects.create(
                    user=existing_user, school=school, role='teacher', state='ACTIVE'
                )
                created.append({'row': i, 'name': name, 'status': 'existing_user_added'})
                continue
            
            # Create new user
            names = name.split(' ', 1)
            first_name = names[0]
            last_name = names[1] if len(names) > 1 else ''
            username = f"teacher_{phone.replace('+', '').replace(' ', '')}"
            
            try:
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone,
                    email=email or None,
                    role='teacher',
                    tsc_number=tsc or None,
                )
                user.set_password(phone[-6:])  # Default password: last 6 digits of phone
                user.save()
                
                # Create profile
                UserProfile.objects.get_or_create(user=user)
                
                # Create membership
                OrganizationMembership.objects.create(
                    user=user, school=school, role='teacher', state='ACTIVE'
                )
                
                # Create specialties
                if specialties_str:
                    from curriculum.models import Subject
                    for spec_name in specialties_str.split(','):
                        spec_name = spec_name.strip()
                        subject = Subject.objects.filter(name__iexact=spec_name).first()
                        if subject:
                            TeacherSpecialty.objects.get_or_create(
                                teacher=user, subject=subject, school=school
                            )
                
                created.append({'row': i, 'name': name, 'status': 'created'})
            except Exception as e:
                errors.append({'row': i, 'error': str(e)})
        
        return created, errors

    @staticmethod
    def import_students(school, stream, academic_year, rows):
        \"\"\"Import students from parsed rows into a specific stream. Returns (created_count, errors).\"\"\"
        from Resources.models import User, UserProfile
        
        created = []
        errors = []
        
        for i, row in enumerate(rows, start=2):
            name = row.get('student_name', '') or row.get('name', '')
            adm_no = row.get('admission_number', '') or row.get('adm_no', '') or row.get('admission_no', '')
            
            if not name:
                errors.append({'row': i, 'error': 'Student name is required'})
                continue
            if not adm_no:
                errors.append({'row': i, 'error': 'Admission number is required'})
                continue
            
            # Check duplicate admission number within this school
            existing_enrollment = StudentEnrollment.objects.filter(
                stream__school_class__school=school,
                student__admission_number=adm_no
            ).first()
            if existing_enrollment:
                errors.append({'row': i, 'error': f'Admission number {adm_no} already exists in this school'})
                continue
            
            names = name.split(' ', 1)
            first_name = names[0]
            last_name = names[1] if len(names) > 1 else ''
            username = f"student_{school.id}_{adm_no}"
            
            try:
                user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    admission_number=adm_no,
                    role='student',
                )
                user.set_password(adm_no)  # Default password: admission number
                user.save()
                
                UserProfile.objects.get_or_create(user=user)
                
                OrganizationMembership.objects.create(
                    user=user, school=school, role='student', state='ACTIVE'
                )
                
                StudentEnrollment.objects.create(
                    student=user, stream=stream, academic_year=academic_year, status='active'
                )
                
                created.append({'row': i, 'name': name, 'adm_no': adm_no, 'status': 'created'})
            except Exception as e:
                errors.append({'row': i, 'error': str(e)})
        
        return created, errors
"""

content += new_services

with open("organizations/services.py", "w") as f:
    f.write(content)

print("Patched services.py")
