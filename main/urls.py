from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='mainUrl'),
    path('contact', views.contacts, name='contactUrl'),
    path('cats', views.cats, name = 'catsUrl'),
    path('sold_cats', views.sold_cats, name = 'sold_catsUrl'),
    path('cat/<int:cat_id>', views.cat_detail, name = 'cat_detail_url'),
]
