from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]

# мой комментарий2
# мой комментарий3
# мой комментарий4
