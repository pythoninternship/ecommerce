from django.urls import path
from . import views
app_name='eapp'
urlpatterns = [
    path('',views.allProductCategory, name='allProductCategory'),
    path('<slug:c_slug>/',views.allProductCategory,name='product_by_category'),
    path('<slug:c_slug>/ <slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]