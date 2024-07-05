from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'landing/landing.html')

def learn_more(request):
    return render(request, 'landing/learn_more.html')
    