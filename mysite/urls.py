from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include("todolist.urls")),
     path('account/', include("users.urls")),
    
]

# ✅ correct way to serve static files in DEBUG
urlpatterns += staticfiles_urlpatterns()
