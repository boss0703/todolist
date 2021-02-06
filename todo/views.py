from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ListForm
from .models import List


def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todoリストにアイテムを追加しました。')

    all_items = List.objects.all
    return render(request, 'todo/index.html', {'all_items': all_items})


def about(request):
    context = {'first_name': 'keita', 'last_name': 'kameoka'}
    return render(request, 'todo/about.html', context)


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Todoリストのアイテムを削除しました。')
    return redirect('index')


def uncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('index')


def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('index')


def edit(request, list_id):
    item = List.objects.get(pk=list_id)
    if request.method == 'POST':
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Todoリストのアイテムを編集しました。')
            return redirect('index')
    else:
        return render(request, 'todo/edit.html', {'item': item})
