from django.urls import path

from . import views

app_name = 'ordenofthesith'
urlpatterns = [
    path('', views.index, name='index'),
    path('rookie/', views.CreateRookie.as_view(), name='rookie'),
    path('rookie/<int:rookie_id>/planet/<int:planet_id>/', views.blackHandTest, name='blackHandTest'),
    path('sith/', views.SithListView.as_view(), name='sith'),
    path('sith/<int:sith_id>/', views.showRookies, name='showRookies'),
    path('sith/<int:sith_id>/rookie/<int:rookie_id>/', views.showAnswers, name='showAnswers'),
    path('sith/count/', views.showSithCount, name='showSithCount'),
    path('sith/one/', views.sithRookieOne, name='sithRookieOne'),
]