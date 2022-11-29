from datetime import date

import pytest

from vacancies.models import Skill


@pytest.mark.django_db
def test_create_vacancy(client, hr_token):
    expected_response = {
        "id": 1,
        "slug": "123",
        "text": "123",
        "status": "draft",
        "created": date.today().strftime("%Y-%m-%d"),
        "user": None,
        "skills": ["test"],
        "likes": 0,
        "min_experience": None,
        "updated_at": None
    }

    data = {
        "slug": "123",
        "text": "123",
        "status": "draft"
    }

    #Skill.objects.create(name="test")

    response = client.post(
        "/vacancy/create/",
        data,
        format="json",
        HTTP_AUTHORIZATION="Token " + hr_token,
        _mutable=True
    )

    assert response.status_code == 201
    assert response.data == expected_response
