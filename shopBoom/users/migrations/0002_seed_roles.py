from django.db import migrations


def create_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    for name in ["ADMIN", "CUSTOMER", "WAREHOUSE"]:
        Role.objects.get_or_create(rolename=name)


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]
