"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from drapi import views
from rest_framework .routers import DefaultRouter


# if follow step 6(Model View Set er shahajje CURD kora) then need under line of code or path use
router = DefaultRouter()
router.register('aiquest', views.AiquwstModelViewSet, basename='teacher')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # if follow step 6(Model View Set er shahajje CURD kora) then need under line of code or path use
    path('', include(router.urls)),
    

    # if follow step 4/5(ListModelMixin in Rest /Concrete View class er shahajje CURD kora) then need under line of code or path use
    # path('ailist/', views.Aiquwst_list_create.as_view(), name='ailistcreate'), # ListModelMixin in Rest howay eita lagbe indivisual data get kora jabe
    # path('ailist/<int:pk>/', views.Aiquest_up_del.as_view(), name='Aiquestupdel'),
    
    # if follow step 3(Class Based View APIView er shahajje CURD kora) then need under line of code or path use
    # path('aicreate/', views.AiquestCrearte.as_view(), name='aicreate'),
    # path('aicreate/<int:pk>', views.AiquestCrearte.as_view(), name='aicreate'), # Class Based View APIView howay eita lagbe indivisual data get kora jabe
    
    # if follow step 2(normaly api view er shahajje CURD kora) then need under line of code or path use
    # path('aicreate/', views.aiquest_create, name='aicreate'),
    # path('aicreate/<int:pk>', views.aiquest_create, name='aicreate'), # api view howay eita lagbe indivisual data get kora jabe
    
    
    # if follow step 1(normaly CURD kora) then need under line of code or path use
    # path('aiinfo/', views.aiquest_info),
    #  path('aiinfo/create/', views.aiquest_create, name='aiquest-create'), 
    # path('aiinfo/<int:pk>', views.aiquest_info_per_data), #api view hole eita lagbe na
]
