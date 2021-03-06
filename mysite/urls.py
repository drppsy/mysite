"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import xadmin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from mysite import views

from mysite.settings.base import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from goods.views import GoodsListViewSet,CategoryViewset

router = DefaultRouter()

#配置goods的url
router.register('goods',GoodsListViewSet,basename='goods')

#配置categorys的url
router.register('categorys',CategoryViewset,basename='categorys')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',views.home,name = 'home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('comment/', include('comment.urls')),
    path('login/',views.login,name = 'login'),
    path('register/', views.register, name='register'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url('', include(router.urls)),
    url('docs/', include_docs_urls(title="接口文档")),
    # JWT的认证接口
    url('loginfortest/', obtain_jwt_token),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)