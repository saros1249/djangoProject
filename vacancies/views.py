import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from djangoProject import settings
from vacancies.models import Vacancy, Skill
from vacancies.serealizers import VacancyListSerializer, VacancyDetailSerializer, VacancyCreateSerializer, \
    VacancyUpdateSerializer, VacancyDestroySerializer


class SkillsListView(ListView):
    model = Skill

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")

        response = []
        for skill in self.object_list:
            response.append({
                "id": skill.id,
                "name": skill.name
            })

        return JsonResponse(response, safe=False)


class SkillDetailView(DetailView):
    model = Skill

    def get(self, request, *args, **kwargs):
        skill = self.get_object()

        return JsonResponse({
            "id": skill.id,
            "name": skill.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class SkillCreateView(CreateView):
    model = Skill
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        skill = Skill.objects.create(
            name=data["name"],
        )

        return JsonResponse({
            "id": skill.id,
            "name": skill.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class SkillUpdateView(UpdateView):
    model = Skill
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        self.object.name = data["name"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class SkillDeleteView(DeleteView):
    model = Skill
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted successfully"}, status=200)


class VacanciesListView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer


class VacancyDetailView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer


class VacancyCreateView(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer


class VacancyUpdateView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer


class VacancyDeleteView(DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDestroySerializer
