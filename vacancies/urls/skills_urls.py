from django.urls import path

from vacancies import views

urlpatterns = [
    path("", views.SkillsListView.as_view(), name='skills'),
    path("create/", views.SkillCreateView.as_view(), name='create_ckill'),
    path("<int:pk>/update/", views.SkillUpdateView.as_view(), name='update_skill'),
    path("<int:pk>/delete/", views.SkillDeleteView.as_view(), name='delete_skill'),
]