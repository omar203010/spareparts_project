from django.shortcuts import render, get_object_or_404, redirect
from .models import CarPart
from .forms import CarPartForm

def car_part_list(request):
    parts = CarPart.objects.all()
    return render(request, 'parts/list.html', {'parts': parts})

def edit_car_part(request, pk):
    part = get_object_or_404(CarPart, pk=pk)
    if request.method == 'POST':
        form = CarPartForm(request.POST, request.FILES, instance=part)
        if form.is_valid():
            form.save()
            return redirect('car_part_list')
    else:
        form = CarPartForm(instance=part)
    return render(request, 'parts/edit.html', {'form': form, 'part': part})

def delete_car_part(request, pk):
    part = get_object_or_404(CarPart, pk=pk)
    if request.method == 'POST':
        part.delete()
        return redirect('car_part_list')
    return render(request, 'parts/delete_confirm.html', {'part': part})
