from django.urls import path

from vacancies import views

urlpatterns = [
    path("", views.VacanciesListView.as_view(), name='vacancies'),
    path("<int:pk>/", views.VacancyDetailView.as_view(), name="detail_vacancies_by_user"),
    path("create/", views.VacancyCreateView.as_view(), name='create_vacancy'),
    path("<int:pk>/update/", views.VacancyUpdateView.as_view(), name='update_vacancy'),
    path("<int:pk>/delete/", views.VacancyDeleteView.as_view(), name='delete_vacancy'),
    path("like/", views.VacancyLikeView.as_view(), name='like_counter')
]