from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),  # 全てのURLに対してtodo.urlsファイルを呼び出す
]
