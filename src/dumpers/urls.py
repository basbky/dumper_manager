from django.urls import path

from .views import DumpersListView

urlpatterns = [
    path('dumpers/', DumpersListView.as_view(), name='dumpers_list'),
]

