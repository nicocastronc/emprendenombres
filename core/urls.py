#CORE URL CONFIGURATION

#from django.contrib import admin
from django.urls import path
#Para acceder a los metodos de vista de generador:
from generador import views

#DEPLOY
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('nombre/',views.nombre,name='nombre'),
    path('about/',views.about,name='about')
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


