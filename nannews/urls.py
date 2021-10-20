from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("catagory/", views.catagory, name="catagory"),
    path("catagory/<str:slug>/", views.catagory, name="catagory"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("detail/", views.detail, name="detail"),
    path("detail/<int:idt>/", views.detail),
    path('checkup/', views.checkup, name='checkup'),
    path('registerEmail/', views.registerEmail , name='registerEmail')
]
