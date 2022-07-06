from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favorite/', include('favorite.urls'), name="favorite"),
    path('login/', auth_views.LoginView.as_view(template_name='lauth/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('organism.urls'), name='home'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('pizza/', include('pizza.urls'), name='pizza'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
