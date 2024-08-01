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

    path('adminMIS/offline.html', views.offline, name='offline'),

    path('adminMIS/offlineUpdate.html', views.offlineUpdate, name='offlineUpdate'),

    path('adminMIS/consultancies.html', views.consultancies, name='consultancies'),

    path('adminMIS/consultanciesUpdate.html', views.consultanciesUpdate, name='consultanciesUpdate'),

    path('addCppp/', views.addCppp, name='addCppp'),

    path('addGem/', views.addGem, name='addGem'),

    path('addOffline/', views.addOffline, name='addOffline'),

    path('addConsultancy', views.addConsultancy, name='addConsultancy'),

    path('adminMIS/cpppStatus.html', views.cpppStatus, name='cpppStatus'),

    path('adminMIS/cpppStatus/<int:pk>/', views.cpppDetail, name='cpppDetail'),

    path('adminMIS/gemStatus.html', views.gemStatus, name='gemStatus'),

    path('adminMIS/gemStatus/<int:pk>/', views.gemDetail, name='gemDetail'),

    path('adminMIS/offlineStatus.html', views.offlineStatus, name='offlineStatus'),

    path('adminMIS/offlineStatus/<int:pk>/', views.offlineDetail, name='offlineDetail'),


    path('adminMIS/consultanciesStatus.html', views.consultanciesStatus, name='consultanciesStatus'),

    path('adminMIS/consultanciesStatus/<int:pk>/', views.consultanciesDetail, name='consultanciesDetail'),

    path('adminMIS/cpppStatus/<int:pk>/edit/', views.cpppEdit, name='cpppEdit'),

    path('adminMIS/gemStatus/<int:pk>/edit/', views.gemEdit, name='gemEdit'),

    path('adminMIS/offlineStatus/<int:pk>/edit/', views.offlineEdit, name='offlineEdit'),

    path('adminMIS/consultanciesStatus.html/<int:pk>/edit/', views.consultanciesEdit, name='consultanciesEdit'),

    path('adminMIS/construction.html', views.construction, name='construction'),
]
