from django.shortcuts import redirect, render
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import Daerah, RumahSakit
from .forms import DaerahForm, RumahSakitForm
from django.contrib import messages;

def index(request):
   list_daerah = Daerah.objects.all().values()
   list_rs = RumahSakit.objects.all().values()
   response = {'list_daerah':list_daerah, 'list_rs':list_rs}
   return render(request, "main.html", response)

def add_rs(request):
    list_daerah = Daerah.objects.all().values()
    list_rs = RumahSakit.objects.all().values()
    form = RumahSakitForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        messages.success(request, 'Rumah Sakit Baru Berhasil Ditambahkan')
    
    if ((not(form.is_valid())) and request.method == 'POST'):
        messages.error(request, 'Rumah Sakit Sudah Ada')
    response = {'form': form, 'list_rs':list_rs, 'list_daerah':list_daerah}
    return render(request, 'add_rs.html', response)

def add_daerah(request):
    list_daerah = Daerah.objects.all().values()
    form = DaerahForm(request.POST or None)
    
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        messages.success(request, 'Daerah Baru Berhasil Ditambahkan')
    
    if ((not(form.is_valid())) and request.method == 'POST'):
        messages.error(request, 'Daerah Sudah Ada')

    response = {'form': form, 'list_daerah': list_daerah}
    return render(request, 'add_daerah.html', response)

def daerah_json(request):
    data = serializers.serialize('json', RumahSakit.objects.all())
    return HttpResponse(data, content_type="application/json")