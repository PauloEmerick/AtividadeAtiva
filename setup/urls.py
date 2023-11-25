
from django.contrib import admin
from django.urls import path

from padaria.views import PadariaListView, PadariaCreateView, PadariaUpdateView, PadariaDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", PadariaListView.as_view(), name="padaria_home"),
    path("create", PadariaCreateView.as_view(), name="padaria_cadastrar"),
    path("update/<int:pk>", PadariaUpdateView.as_view(), name="padaria_editar"),
    path("delete/<int:pk>", PadariaDeleteView.as_view(), name="padaria_excluir"),

    
]
