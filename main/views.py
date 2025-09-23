from django.shortcuts import render, redirect, get_object_or_404
from main.forms import FootballProductsForm
from main.models import FootballProducts
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        football_products = FootballProducts.objects.all()
    else:
        football_products = FootballProducts.objects.filter(user=request.user)

    context = {
        'npm' : '2406365326',
        'name': request.user.username,
        'class': 'PBP KKI',
        'football_products' : football_products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_football_product(request):
    form = FootballProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        football_product = form.save(commit=False)   
        football_product.user = request.user         
        football_product.save()                      
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "create_football_product.html", context)

@login_required(login_url='/login')
def product_details(request, id):
    product = get_object_or_404(FootballProducts, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_details.html", context)

def show_xml(request):
    data = FootballProducts.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    data = FootballProducts.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        data = FootballProducts.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    except FootballProducts.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        data = FootballProducts.objects.filter(pk=id)
        json_data = serializers.serialize("json", data)
        return HttpResponse(json_data, content_type="application/json")
    except FootballProducts.DoesNotExist:
        return HttpResponse(status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response