from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406365326',
        'name': 'Sultanadika Shidqi Mumtazsami',
        'class': 'KKI'
    }

    return render(request, "main.html", context)