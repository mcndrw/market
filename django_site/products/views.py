from django.http import HttpResponse        
from django.views import generic 
from .models import Product
from .models import Category

def index(request): 
    return HttpResponse("Welcome to PhotoScrub Shop!")
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class ProductListView(generic.ListView):
    template_name = 'products_list.html'
    context_object_name = 'products' 
    model = Product 
    
class ProductDetailView(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product

class CategoryView(generic.DetailView):
    template_name = 'category.html'
    context_object_name = 'category'
    model = Category
