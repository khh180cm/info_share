from django.urls import path

from topic import views


urlpatterns = [
    path('brand/', views.BrandSearch.as_view(), \
        name='brand-list'),
    path('topic/<int:pk>/', views.TopicDetail.as_view(), \
        name='topic-detail'),
]
