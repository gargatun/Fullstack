from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import InquiryForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
        else:
            print(form.errors)  # Выведите ошибки формы в консоль
    else:
        form = InquiryForm()
    return render(request, 'index.html', {'form': form})


def about_complex(request):
    return render(request, 'about_complex.html')

def district(request):
    # Логика обработки запроса для страницы "Район"
    return render(request, 'district.html')

def apartment_catalog(request):
    # Логика обработки запроса для страницы "Каталог квартир"
    return render(request, 'apartment_catalog.html')

def mortgage(request):
    # Логика обработки запроса для страницы "Ипотека"
    return render(request, 'mortgage.html')

def contacts(request):
    # Логика обработки запроса для страницы "Контакты"
    return render(request, 'contacts.html')

def sectionmap(request):
    # Логика обработки запроса для страницы "Контакты"
    return render(request, 'sectionmap.html')

def success_view(request):
    return render(request, 'index.html')  # Указывает на шаблон, который отображает страницу успеха