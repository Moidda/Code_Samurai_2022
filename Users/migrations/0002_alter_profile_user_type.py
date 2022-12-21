# Generated by Django 4.1.4 on 2022-12-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('SYSADMIN', 'System Admin'), ('ECNEC', 'Executive Committee of National Economic Council'), ('MOP', 'Ministry of Planning'), ('EXEC', 'Executing Agency'), ('APP', 'Application Users')], max_length=50, null=True),
        ),
    ]
