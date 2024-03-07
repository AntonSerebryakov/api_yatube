from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, api_comment_detail, api_comment

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/posts/<int:post_id>/comments/<int:comment_id>/',
         api_comment_detail),
    path('v1/posts/<int:post_id>/comments/', api_comment),
    path('v1/', include(router_v1.urls)),

]
