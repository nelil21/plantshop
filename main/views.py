from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'PlantShop',
        'npm' : '2306123456',
        'name': 'Nelil Amaani',
        'class': 'PBP E',
    }
    return render(request, 'main/main.html', context)
