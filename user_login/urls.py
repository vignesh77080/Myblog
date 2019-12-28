from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'user_login'

urlpatterns = [

    path('', views.home , name = 'home-page' ),
    path('register/', views.register , name = 'register' ),
    path('profile/', views.profile , name = 'profile' ),
    path('createpost/', views.createpost , name = 'createpost' ),
    path('editpost/<int:post_id>/', views.editpost , name = 'editpost' ),
    path('viewpost/<int:post_id>/', views.viewpost , name = 'viewpost' ),
    path('deletepost/<int:post_id>/', views.deletepost , name = 'deletepost' ),

]

