from django.urls import path
from . import views
urlpatterns = [
    path('add',views.add),

    path('select',views.select),

    path('select2',views.select2),

    path('update',views.update),

    path('delete',views.delete)
]