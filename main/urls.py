from django.urls import path
from main.views import create_product_flutter, show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, add_product_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
from main.views import home, products, categories, cart
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('', home, name='home'),  # URL untuk home
    path('products/', products, name='products'),  # URL untuk produk
    path('categories/', categories, name='categories'),  # URL untuk kategori
    path('cart/', cart, name='cart'),  # URL untuk keranjang
    path('add-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('create-product/', create_product_flutter, name='create_product_flutter'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
