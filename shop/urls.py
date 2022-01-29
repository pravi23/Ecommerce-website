from django.urls import path
from.import views


urlpatterns=[
    path('',views.index,name='index'),
    path('<slug:c_slug>/',views.index,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetails,name='details'),
    path('search',views.search,name='search')

]