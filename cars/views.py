from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Car

# Create your views here.
def index(request):
    print request.subdomain
    car = get_object_or_404(Car, slug=request.subdomain)
    data = {}
    if car.broken:
        data['broken'] = 'YES'
    else:
        data['broken'] = 'NO'
    return render(request, 'index.html', data)