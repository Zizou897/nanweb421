from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.index, name="index"),
    path("catagory/", views.catagory, name="catagory"),
    path("catagory/<str:cat>/", views.catagory, name="catagory"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("detail/", views.detail, name="detail"),
    path("detail/<int:idt>/", views.detail),
    path('checkup/', views.checkup, name='checkup'),
    path('registerEmail/', views.registerEmail , name='registerEmail')
]
