from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]