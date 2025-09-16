from django.shortcuts import render, redirect, get_object_or_404
from main.forms import FootballProductsForm
from main.models import FootballProducts
from django.core import serializers
from django.http import HttpResponse

def show_main(request):
    Football_products = FootballProducts.objects.all()

    context = {
        'npm' : '2406365326',
        'name': 'Sultanadika Shidqi M',
        'class': 'PBP KKI',
        'football_products' : Football_products,
    }

    return render(request, "main.html", context)

def create_football_product(request):
    form = FootballProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_football_product.html", context)

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
