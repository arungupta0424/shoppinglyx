from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import CustLoginForm, CustPassChangeForm, CustPassResetForm, CustPassSetForm

urlpatterns = [
    # path('', views.home),

    path('', views.ProductView.as_view(), name='home'),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=CustPassChangeForm, success_url='/changepassdone/'), name='changepassword'),

    path('changepassdone/', auth_views.PasswordChangeDoneView.as_view(template_name="app/passwordchangedone.html"), name='changepassdone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="app/password_reset.html", form_class=CustPassResetForm), name="password_reset"),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=CustPassSetForm), name="password_reset_confirm"),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"), name="password_reset_complete"),


    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=CustLoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustRegView.as_view(),  name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
