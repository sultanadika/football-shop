from django.shortcuts import render, redirect, get_object_or_404
from main.forms import FootballProductsForm,CarForm
from main.models import FootballProducts,Car
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        football_products = FootballProducts.objects.all()
    else:
        football_products = FootballProducts.objects.filter(user=request.user)

    context = {
        'npm' : '2406365326',
        'name': 'Sultanadika Shidqi M',
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

from django.http import JsonResponse
from .models import FootballProducts

def show_json(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "my" and request.user.is_authenticated:
        products = FootballProducts.objects.filter(user=request.user)
    else:
        products = FootballProducts.objects.all()

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category if hasattr(product, 'category') else None,
            'created_at': product.created_at.isoformat() if hasattr(product, 'created_at') and product.created_at else None,
            'user_id': product.user.id if product.user else None,
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, id):
    try:
        data = FootballProducts.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    except FootballProducts.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product = FootballProducts.objects.select_related('user').get(pk=id)
        data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'brand': getattr(product, 'brand', None),
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': getattr(product, 'is_featured', False),
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else 'Anonymous',
            'user_is_owner': request.user.is_authenticated and product.user == request.user,
        }
        return JsonResponse(data)
    except FootballProducts.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle AJAX (for your fetch() in register.html)
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True})
            # fallback for non-AJAX
            return redirect("main:login")
        else:
            # Handle validation errors
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                error_messages = []
                for field, errors in form.errors.items():
                    for error in errors:
                        error_messages.append(f"{field.capitalize()}: {error}")
                error_text = " | ".join(error_messages) if error_messages else "Registration failed."
                return JsonResponse({"success": False, "error": error_text}, status=400)
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', datetime.datetime.now().strftime("%b %d, %Y %H:%M"))

            # ✅ Return JSON if AJAX, else normal redirect
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return response
        else:
            # Invalid form
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Invalid username or password.'}, status=400)
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect('main:show_main')  # or your login page
    response.set_cookie('showLogoutToast', 'true', max_age=5)
    return response

def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)

        if form.is_valid():
            car_form = Car.objects.create(name = form.cleaned_data["name"],
            brand = form.cleaned_data["brand"],
            stock = form.cleaned_data["stock"])
            return render(request, "create_car.html", {"form": form, "car_form": car_form})
    else:
        form = CarForm()
        return render(request, "create_car.html", {"form": form})

def edit_product(request, id):
    product = get_object_or_404(FootballProducts, pk=id)
    form = FootballProductsForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
    'form': form
    }

    return render(request, "edit_footballshop.html", context)

def delete_product(request, id):
    product = get_object_or_404(FootballProducts, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def about_shop(request):
    return render(request, "about_shop.html")

def contact_shop(request):
    return render(request, "contact_shop.html")

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    category = request.POST.get("category")
    brand = request.POST.get("brand")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user if request.user.is_authenticated else None

    # Create new product
    new_product = FootballProducts(
        name=name,
        description=description,
        price=price or 0,
        category=category,
        brand=brand,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)