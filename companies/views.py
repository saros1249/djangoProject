import json


from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from companies.models import Company


class CompaniesListView(ListView):
    model = Company

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")

        response = []
        for company in self.object_list:
            response.append({
                "id": company.id,
                "name": company.name,
                "logo": str(company.logo)
            })


        return JsonResponse(response, safe=False)


class CompanyDetailView(DetailView):
    model = Company

    def get(self, request, *args, **kwargs):
        company = self.get_object()

        return JsonResponse({
            "id": company.id,
            "name": company.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class CompanyCreateView(CreateView):
    model = Company
    fields = ["name", "logo"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        company = Company.objects.create(
            name=data["name"],
            logo=data["logo"]
        )

        return JsonResponse({
            "id": company.id,
            "name": company.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class CompanyUpdateView(UpdateView):
    model = Company
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
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted successfully"}, status=200)
