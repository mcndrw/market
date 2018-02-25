from django.contrib import admin
from django.urls import path
from products import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('categorys/<int:pk>/', views.CategoryView.as_view(), name='category'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)