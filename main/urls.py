from django.urls import path
from main.views import show_main, create_football_product, create_car, product_details, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, about_shop, contact_shop

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_football_product, name='create_football_product'),
    path('product/<str:id>/', product_details, name='product_details'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('product/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('product/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-car/', create_car, name= "create_car"),
    path('product/<int:id>/edit-product/',edit_product, name="edit_product"),
    path('product/<int:id>/delete-product/',delete_product, name="delete_product"),
    path('about-shop/', about_shop, name="about_shop"),
    path('contact-shop/',contact_shop, name="contact_shop"),
]

