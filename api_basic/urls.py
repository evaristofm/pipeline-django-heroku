from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserViewSet, basename='articles')




urlpatterns = [
    path('api/', include(router.urls)),
   # path('articles/', views.ArticleApiView.as_view()),
   # path('articles/', views.GenericApiView.as_view()),
   # path('articles/<int:id>/', views.GenericApiView.as_view()),
   # path('articles/<int:id>/', views.ArticleDetail.as_view()),
]


