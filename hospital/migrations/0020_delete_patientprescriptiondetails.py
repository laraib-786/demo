# Generated by Django 3.2.9 on 2022-01-11 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_patientprescriptiondetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientPrescriptionDetails',
        ),
    ]