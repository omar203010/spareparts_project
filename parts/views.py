from django.shortcuts import render, redirect
from .forms import CarPartForm
from .models import CarPart

def upload_car_part(request):
    if request.method == 'POST':
        form = CarPartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_part_list')
    else:
        form = CarPartForm()
    return render(request, 'upload.html', {'form': form})

def car_part_list(request):
    parts = CarPart.objects.all()
    return render(request, 'list.html', {'parts': parts})
