
from django.urls import path
from .views import *
urlpatterns = [
    path('palestras', PalestraListView.as_view(), name="palestras"),
    path('palestras/<int:pk>', PalestraDetailView.as_view(), name='palestra-detail'),
    path('palestras/create/', PalestraCreate.as_view(), name='palestra_create'),
    path('palestras/<int:pk>/update/',PalestraUpdate.as_view(), name='palestra_update'),
    path('palestras/<int:pk>/delete/', PalestraDelete.as_view(), name='palestra_delete'),
    
]