from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import main.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', main.views.index, name='index'),
    path('account/', main.views.account, name='account'),
    path('create_account/', main.views.create_account, name='create_account'),
    path('logout/', main.views.user_logout, name='user_logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
