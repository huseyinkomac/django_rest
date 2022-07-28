from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# First approach

# game_list = views.GameViewSet.as_view({
#     'get': 'list'
# })

# game_create = views.GameViewSet.as_view({
#     'post': 'create'
# })

# game_detail = views.GameViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })


# urlpatterns = [
#     path('', game_list, name='game-list'),
#     path('create', game_create, name='game-create'),
#     path('<int:pk>/', game_detail, name='game-detail'),
# ]


# Second Approach

# router = DefaultRouter()
# router.register('', views.GameViewSet, basename="games")

# urlpatterns = [
#     path('', include(router.urls)),
# ]


# Third approach

urlpatterns = [
    path('', views.GameListView.as_view(), name='game-list'),
    path('create/', views.GameCreateView.as_view(), name='game-create'),
    path('<int:pk>/', views.GameDetailView.as_view(), name='game-detail'),
]
