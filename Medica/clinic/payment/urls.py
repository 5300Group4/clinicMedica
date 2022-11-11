from django.urls import path

from . import views

urlpatterns = [
    path('checkout/', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session),  # new
    path('success/', views.SuccessView.as_view()),  # new
    path('cancelled/', views.CancelledView.as_view()),  # new
    
]
