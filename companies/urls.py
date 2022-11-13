from django.urls import path

from companies import views

urlpatterns = [
    path("", views.CompaniesListView.as_view(), name='companies'),
    path("create/", views.CompanyCreateView.as_view(), name='create_company'),
    path("<int:pk>/update/", views.CompanyUpdateView.as_view(), name='update_company'),
    path("<int:pk>/delete/", views.CompanyDeleteView.as_view(), name='delete_company'),
]