# Generated by Django 3.2.7 on 2022-03-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_student_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='standard',
            field=models.CharField(default='Not Mention', max_length=10),
        ),
    ]
