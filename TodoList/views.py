from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('O item foi adicionado à seus afazeres!'))
            return render(request, 'index.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'index.html', {'all_items': all_items})
def delete(request, List_id):
    item = List.objects.get(pk=List_id)
    item.delete()
    messages.success(request, ("Item deletado!"))
    return redirect('index.html')

def cross_off(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = True
    item.save()
    return redirect('index.html')

def uncross(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = False
    item.save()
    return redirect('index.html')
def editar(request, List_id):
    if request.method == 'POST':
        item = List.objects.get(pk=List_id)

        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa editada com sucesso!')
            return redirect('index.html')
    else:
        item = List.objects.get(pk=List_id)
        return render(request, 'edit.html', {'item': item})
