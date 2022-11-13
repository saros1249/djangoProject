import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from vacancies.models import Vacancy, Skill


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


class VacanciesListView(ListView):
    model = Vacancy

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        search_text = request.GET.get("text", None)
        if search_text:
            self.object_list = self.object_list.filter(text=search_text)

        response = []
        for vacancy in self.object_list:
            response.append({
                "id": vacancy.id,
                "text": vacancy.text
            })
        return JsonResponse(response, safe=False)


class VacancyDetailView(DetailView):
    model = Vacancy

    def get(self, request, *args, **kwargs):
        vacancy = self.get_object()

        return JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })


@method_decorator(csrf_exempt, name="dispatch")
class VacancyCreateView(CreateView):
    model = Vacancy
    fields = ["user", "slug", "text", "status", "created", "skills"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        vacancy = Vacancy.objects.create(
            user_id=data["user_id"],
            slug=data["slug"],
            text=data["text"],
            status=data["status"]
        )

        return JsonResponse({
            "id": vacancy.id,
            "slug": vacancy.slug,
            "text": vacancy.text,
            "status": vacancy.status
        })


@method_decorator(csrf_exempt, name="dispatch")
class VacancyUpdateView(UpdateView):
    model = Vacancy
    fields = ["text", "status"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        self.object.text = data["text"]
        self.object.status = data["status"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "slug": self.object.slug,
            "text": self.object.text,
            "status": self.object.status
        })


@method_decorator(csrf_exempt, name="dispatch")
class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted successfully"}, status=200)
