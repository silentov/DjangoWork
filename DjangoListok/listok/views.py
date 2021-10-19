from django.shortcuts import render
from .models import User
from .forms import UserForm


def clients(request):
    personal = User.objects.order_by('FIO')
    context = {
        'personal': personal,
        'title': 'Список персонала',
    }
    return render(request, 'app_templates/form.html', context)


def add_client(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            personal = form.save()
    else:
        form = UserForm()
    return render(request, 'app_templates/add_client.html', {'form': form})