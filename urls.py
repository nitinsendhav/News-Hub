from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('india/', views.india, name='india'),
    path('bollywood/', views.bollywood, name='bollywood'),
    path('sport/', views.sport, name='sport'),
    path('online/', views.online, name='online'),
    path('search/', views.search, name='search'),
    path('detail/<int:pk>/', views.news_detail, name='detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
