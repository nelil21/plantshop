import json
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

#fungsi untuk show main
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': 'Nelil Amaani',
        'class': 'PBP B',
        'npm': '2306227835',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'main.html', context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None, request.FILES or None)  # Include request.FILES

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = ProductEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    product = ProductEntry.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def home(request):
    return render(request, 'main/home.html')  # Ganti dengan template yang sesuai

def products(request):
    return render(request, 'main/products.html')

def categories(request):
    return render(request, 'main/categories.html')

def cart(request):
    return render(request, 'main/cart.html')

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    stock = request.POST.get("stock")
    difficulty = request.POST.get("difficulty")
    user = request.user
    
    new_product = ProductEntry(
        name=name, 
        price=price,
        description=description,
        stock=stock,
        difficulty=difficulty,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            # Parsing JSON dari request.body
            data = json.loads(request.body)

            # Membuat entri produk baru
            new_product = ProductEntry.objects.create(
                user=request.user,  # Menggunakan pengguna saat ini
                name=data["name"],  # Nama produk
                price=int(data["price"]),  # Harga produk
                description=data["description"],  # Deskripsi produk
                stock=int(data["stock"]),  # Stok produk
                difficulty=data["difficulty"],  # Kesulitan produk
            )

            new_product.save()  # Simpan ke database

            return JsonResponse({"status": "success", "message": "Product created successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=401)
