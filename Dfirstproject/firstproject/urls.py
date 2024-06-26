"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from community.views import List, detail

import community.views
import accounts.views 

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:question_id>', detail, name="detail"),
    path('',community.views.List, name='list'),
    path('post/<int:question_id>', community.views.detail, name="detail"),
    path('new/', community.views.new, name="new"),
    path('create/', community.views.create, name="create"),
    path('delete/<int:question_id>', community.views.delete,name="delete"),
    path('update/<int:question_id>', community.views.update,name="update"),
    path('<int:question_id>/comment', community.views.add_comment,name="add_comment"),
    path('accounts/login', accounts.views.login_view, name="login"),
    path('accounts/logout', accounts.views.logout_view,name="logout"),
    path('acconuts/signup', accounts.views.signup_view,name="signup")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)