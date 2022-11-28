from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from vacancies.models import Vacancy, Skill


class NotInStatusValidator:
    def __init__(self, statuses):
        if not isinstance(statuses, list):
            statuses = [statuses]
        self.statuses = statuses

    def __call__(self, value):
        if value not in self.statuses:
            raise serializers.ValidationError("Не корректный статус")


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class VacancyListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Vacancy
        fields = ["id", "text", "slug", "status", "created", "username", "skills"]


class VacancyDetailSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyCreateSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Skill.objects.all(),
        slug_field="name"
    )

    slug = serializers.CharField(
        max_length=50,
        validators=[UniqueValidator(queryset=Vacancy.objects.all())]  # , lookup="contains"
    )

    status = serializers.CharField(max_length=6, validators=[NotInStatusValidator("closed")])

    class Meta:
        model = Vacancy
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        self._skills = self.initial_data.pop("skills", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(**validated_data)

        for skill in self._skills:
            skill_obj, _ = Skill.objects.get_or_create(name=skill)
            vacancy.skills.add(skill_obj)

        vacancy.save()
        return vacancy


class VacancyUpdateSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Skill.objects.all(),
        slug_field="name"
    )
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    created = serializers.DateField(read_only=True)

    class Meta:
        model = Vacancy
        fields = ["id", "text", "slug", "status", "created", "user", "skills"]

    def is_valid(self, raise_exception=False):
        self._skills = self.initial_data.pop("skills", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        vacancy = super().save()

        for skill in self._skills:
            skill_obj, _ = Skill.objects.get_or_create(name=skill)
            vacancy.skills.add(skill_obj)

        vacancy.save()
        return vacancy


class VacancyDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["id"]
