# Generated by Django 3.1.2 on 2020-10-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drug_disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_bank_id', models.CharField(max_length=100)),
                ('pubchem_id', models.CharField(max_length=100)),
                ('drug_name', models.CharField(max_length=100)),
                ('approved_against_diseases_name', models.CharField(max_length=100)),
                ('disease_mesh_id', models.CharField(max_length=100)),
                ('mechanism_of_action', models.CharField(max_length=100)),
            ],
        ),
    ]
