# Generated by Django 3.2.7 on 2022-03-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_student_standard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
