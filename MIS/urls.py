from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='MIS/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('adminMIS/', views.adminMIS, name='adminMIS'),

    path('adminMIS/procurement.html', views.procurement, name='procurement'),

    path('adminMIS/cppp.html', views.cppp, name='cppp'),

    path('adminMIS/cpppUpdate.html', views.cpppUpdate, name='cpppUpdate'),

    path('adminMIS/gem.html', views.gem, name='gem'),

    path('adminMIS/gemUpdate.html', views.gemUpdate, name='gemUpdate'),

    path('addCppp/', views.addCppp, name='addCppp'),

    path('addGem/', views.addGem, name='addGem'),

    path('adminMIS/cpppStatus.html', views.cpppStatus, name='cpppStatus'),

    path('adminMIS/cpppStatus/<int:pk>/', views.cpppDetail, name='cpppDetail'),

    path('adminMIS/gemStatus.html', views.gemStatus, name='gemStatus'),

    path('adminMIS/gemStatus/<int:pk>/', views.gemDetail, name='gemDetail'),
]
