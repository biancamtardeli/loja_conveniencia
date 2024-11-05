<<<<<<< HEAD
from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
=======
from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
>>>>>>> 0267ae72f6c0e577abe401074f101fef5c7173cc
