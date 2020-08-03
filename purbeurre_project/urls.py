"""purbeurre_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', include('pages.urls', namespace="pages")),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace="products")),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls', namespace="account")),
    path('account/profile/', auth_views.LoginView.as_view(template_name='account/index.html', extra_context={'title': 'Ahoy!', 'headerImg': 'header_contact.jpg'}), name='profile'),
    path('sentry-debug/', trigger_error),
]
