from django.urls import path
from .views import index, about, contact, menu, service, testimonial, team, menuDetail, menu2Detail, menu3Detail, \
    teamDetail, testiDetail, MenuCreateView, MenuUpdateView, MenuDeleteView

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('index/', index, name='index'),
    path('menu/', menu, name='menu'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path("menu/<slug:menu>", menuDetail, name='menu_detail_view'),
    path("menu2/<slug:menu2>", menu2Detail, name='menu2_detail_view'),
    path("menu3/<slug:menu3>", menu3Detail, name='menu3_detail_view'),
    path("team/<slug:team>", teamDetail, name='team_detail_view'),
    path("testi/<slug:testi>", testiDetail, name='testi_detail_view'),
    path("menu/create/", MenuCreateView.as_view(), name='menuCreate'),
    path("menu/delete/<slug>/", MenuDeleteView.as_view(), name='menuDelete'),
    path('menu/edit/<slug>/', MenuUpdateView.as_view(), name="menuUpdate"),
    ]