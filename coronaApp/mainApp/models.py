from django.db import models

# Create your models here.
class drug_disease(models.Model):
    drug_bank_id = models.CharField(max_length=100)
    pubchem_id = models.CharField(max_length=100)
    drug_name = models.CharField(max_length=100)
    approved_against_diseases_name = models.CharField(max_length=100)
    disease_mesh_id = models.CharField(max_length=100)
    mechanism_of_action = models.CharField(max_length=100)
