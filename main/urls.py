from django.urls import path
from .views import *
urlpatterns = [
    path('tabletypes/', TableTypeListAPIView.as_view(), name='tabletype-list'),
    path('tabletypes/<int:pk>/', TableTypeDetailAPIView.as_view(), name='tabletype-detail'),
    path('tableinfo/answer/', TableInfoAnswerAPIView.as_view(), name='tableinfo-answer'),
    path('tableinfo/answers/<str:student_number>/', TableInfoAnswerAPIView.as_view(), name='tableinfo-answers'),

]
