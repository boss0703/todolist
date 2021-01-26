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


def delete(request):
    item = List.object.get(pk=list_id)
    item.delete()
    messages.success(request, 'Todoリストのアイテムを削除しました。')
    return redirect('home')
