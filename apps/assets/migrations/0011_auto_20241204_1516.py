# Generated by Django 4.1.13 on 2024-12-04 07:16

from django.db import migrations, models


def migrate_platform_sqlserver_automation(apps, schema_editor):
    platform_model = apps.get_model('assets', 'Platform')
    platform = platform_model.objects.filter(name='SQLServer').first()

    if platform:
        automation = platform.automation
        automation.gather_accounts_method = 'gather_accounts_sqlserver'
        automation.save()


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0010_alter_automationexecution_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name="automationexecution",
            name="status",
            field=models.CharField(
                choices=[
                    ("ready", "Ready"),
                    ("pending", "Pending"),
                    ("running", "Running"),
                    ("success", "Success"),
                    ("failed", "Failed"),
                    ("error", "Error"),
                    ("canceled", "Canceled"),
                ],
                default="pending",
                max_length=16,
                verbose_name="Status",
            ),
        ),
        migrations.RunPython(migrate_platform_sqlserver_automation)
    ]
