from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_buying/', views.add_buying, name='add_buying'),
    path('grades/', views.GradeList.as_view(), name='grades_index'),
    path('grades/<int:pk>/', views.GradeDetail.as_view(), name='grades_detail'),
    path('grades/create/', views.GradeCreate.as_view(), name='grades_create'),
    path('grades/<int:pk>/update/', views.GradeUpdate.as_view(), name='grades_update'),
    path('grades/<int:pk>/delete/', views.GradeDelete.as_view(), name='grades_delete'),
    path('cards/<int:card_id>/assoc_grade/<int:grade_id>/', views.assoc_grade, name='assoc_grade'),
    path('cards/<int:card_id>/unassoc_grade/<int:grade_id>/', views.unassoc_grade, name='unassoc_grade'),
]
