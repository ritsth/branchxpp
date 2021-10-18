from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from myplant.views import QuestionViewSet,UserViewSet,ChoiceViewSet,AllPostsViewSet,NotificationsViewSet,AddPlantViewSet,humidityViewSet,PostsNowViewSet,PostsLaterViewSet,ProfileViewSet,CommentViewSet,nearbyDevicesViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from myplant.views import BlacklistTokenUpdateView
router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions')
router.register('choices', ChoiceViewSet, basename='choices')
router.register('users', UserViewSet, basename='users')
router.register('plants', AddPlantViewSet, basename='plants')
router.register('comment', CommentViewSet, basename='comment')
router.register('posts_now', PostsNowViewSet, basename='posts_now')
router.register('posts_later', PostsLaterViewSet, basename='posts_later')
router.register('profile_photo', ProfileViewSet, basename='profile_photo')
router.register('humidity', humidityViewSet, basename='humidity')
router.register('Notifications', NotificationsViewSet, basename='Notifications')
router.register('nearbyDevices', nearbyDevicesViewSet, basename='nearbyDevices')
router.register('allPosts',AllPostsViewSet, basename='allPosts')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth', obtain_auth_token),
  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
