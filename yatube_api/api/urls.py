from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, api_comment_detail, api_comment

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('posts/<int:post_id>/comments/<int:comment_id>/', api_comment_detail),
    path('posts/<int:post_id>/comments/', api_comment),
    path('', include(router.urls)),

]
