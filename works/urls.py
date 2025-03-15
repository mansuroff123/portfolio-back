from django.urls import path
from .views import WorkList, WorkDetail


urlpatterns = [
    path('works/', WorkList.as_view(), name='works'),
    path('work/<int:pk>/', WorkDetail.as_view(), name='work-detail'),
]