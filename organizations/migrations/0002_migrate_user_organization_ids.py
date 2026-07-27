from django.db import migrations


def migrate_user_organization_ids(apps, schema_editor):
    User = apps.get_model('Resources', 'User')
    School = apps.get_model('organizations', 'School')
    OrganizationMembership = apps.get_model('organizations', 'OrganizationMembership')

    for user in User.objects.filter(organization_id__isnull=False):
        school, _ = School.objects.get_or_create(
            id=user.organization_id,
            defaults={
                'name': f"Migrated School {user.organization_id}",
                'code': f"SCH-{user.organization_id}",
                'contact_email': user.email or f"admin@school{user.organization_id}.com",
                'is_active': True,
            }
        )
        
        valid_roles = ['school_admin', 'teacher', 'student']
        role = user.role if user.role in valid_roles else 'school_admin'
        account_state = getattr(user, 'account_state', 'ACTIVE')
        state = 'ACTIVE' if account_state == 'ACTIVE' else 'PENDING'

        OrganizationMembership.objects.get_or_create(
            user=user,
            school=school,
            defaults={
                'role': role,
                'state': state,
            }
        )


def reverse_migrate(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('Resources', '0040_user_account_state_userprofile_onboarding_complete_and_more'),
    ]

    operations = [
        migrations.RunPython(migrate_user_organization_ids, reverse_migrate),
    ]
