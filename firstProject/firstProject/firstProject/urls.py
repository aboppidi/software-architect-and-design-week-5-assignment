from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('hello/', include('helloWorld.urls')),
	path('admin/', admin.site.urls),
]
