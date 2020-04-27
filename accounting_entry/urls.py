from django.urls import path
from . import views

app_name = 'accounting_entry'

urlpatterns = [
    path('', views.summary_page, name="homepage"),
    path('<int:entry_id>/', views.detail, name="detail"),
    path('add_entry', views.add_entry, name="update"),
]
