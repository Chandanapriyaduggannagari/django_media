from django.urls import path
from apis.v1 import views

urlpatterns = [
    path('get_bookes',views.all_books),
    path("add_book",views.add_book),
    path('edit_book',views.edit_book),
    path('all_book',views.all_book),
    path('delete_book',views.delete_book),
    path('only_one/<int:auth>',views.only_one),


]

