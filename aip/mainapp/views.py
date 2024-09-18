from django.shortcuts import render
from .models import Attraction

def home(request):
    context = {'attraction_list':Attraction.objects.all().order_by('order', 'name').filter(active=True)}
    return render(request, 'home.html', context)
