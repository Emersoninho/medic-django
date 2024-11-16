from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='profiles'),
    path('profile/<int:medic_id>/', views.list_profile_view, name='profile'),
    path('medic/', views.list_medics_view, name='medics'),
    path('favorite/', views.add_favorite_view, name='medic-favorite')
]
