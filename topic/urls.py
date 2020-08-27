from django.urls import path

from topic import views


urlpatterns = [
    path('brand/search', views.BrandSearch.as_view(), \
        name='brand-list'),
    path('topic/<int:pk>/', views.TopicDetail.as_view(), \
        name='topic-detail'),
    path('category/search/', views.CategorySearch.as_view({'get': 'list'}), \
        name='sell-category-list'),


]
