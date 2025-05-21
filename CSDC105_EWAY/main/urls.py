from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage-with-account/', views.homepage_with_account, name='home_page_with_account'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('create-account/', views.create_account, name='create_account'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('signin/', views.signin, name='signin'),
    path('user-registration/', views.user_registration, name='user_registration'),
    path('registration/', views.registration, name='registration'),
    path('showcase-with-account/', views.showcase_with_account, name='showcase_with_account'),
    path('regulations/', views.regulations, name='regulations'),

    # Maintenance pages (added)
    path('maintenance/', views.maintenance_main, name='maintenance_main'),
    path('maintenance/battery/', views.maintenance_battery, name='maintenance_battery'),
    path('maintenance/services/', views.maintenance_services, name='maintenance_services'),
    path('maintenance/tire/', views.maintenance_tire, name='maintenance_tire'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-content/', views.admin_content, name='admin_content'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-registrations/', views.admin_registrations, name='admin_registrations'),
]
