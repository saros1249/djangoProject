import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView

from djangoProject import settings
from vacancies.models import Vacancy, Skill
from vacancies.serealizers import VacancyListSerializer, VacancyDetailSerializer, VacancyCreateSerializer


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


    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #
    #     search_text = request.GET.get("text", None)
    #     if search_text:
    #         self.object_list = self.object_list.filter(text=search_text)
    #
    #     self.object_list = self.object_list.select_related("user").prefetch_related("skills").order_by("text")
    #
    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
    #     page_number = request.GET.get("page")
    #     page_object = paginator.get_page(page_number)
    #
    #     list(map(lambda x: setattr(x, "username", x.user.username if x.user else None), page_object))
    #
    #     response = {
    #         "items": VacancyListSerializer(page_object, many=True).data,
    #         "num_pages": paginator.num_pages,
    #         "total": paginator.count
    #     }

    #    return JsonResponse(response, safe=False)


class VacancyDetailView(DetailView):
    model = Vacancy

    def get(self, request, *args, **kwargs):
        vacancy = self.get_object()

        return JsonResponse(VacancyDetailSerializer(vacancy).data)



@method_decorator(csrf_exempt, name="dispatch")
class VacancyCreateView(CreateView):
    model = Vacancy
    fields = ["user", "slug", "text", "status", "created", "skills"]

    def post(self, request, *args, **kwargs):
        data = VacancyCreateSerializer(data=json.loads(request.body))

        if data.is_valid():
            data.save()
        else:
            return JsonResponse(data.errors)


        return JsonResponse(data.data)


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
