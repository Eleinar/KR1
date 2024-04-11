from django.urls import path
from Var2 import views

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', views.index)
]
