from django.urls import path
from main.views import show_main, create_football_product, product_details, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_football_product, name='create_football_product'),
    path('product/<str:id>/', product_details, name='product_details'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('product/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('product/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]


