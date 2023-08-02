
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path ('', views.home_view, name='home'),
    # path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('delete_task/<int:task_id>/', views.delete_task_view, name='delete_task'),
]