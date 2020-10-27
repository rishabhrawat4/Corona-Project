from django.shortcuts import render
from .models import drug_disease

def home(request):

    dd = drug_disease.objects.all()
    return render(request, "index.html", {'dd': dd})