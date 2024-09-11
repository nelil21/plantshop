from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'PlantShop',
        'npm' : '2306227835',
        'name': 'Nelil Amaani',
        'class': 'PBP B',
    }
    return render(request, 'main/main.html', context)
