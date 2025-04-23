import pytest
from constants import BASE_URL, AUTH_HEADERS, API_HEADERS, AUTH_DATA


class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), "Элемент не создан"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]

        TestItems.created_item_id = item_id

    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"

    def test_update_item(self,auth_session):
        assert hasattr(self.__class__, "created_item_id"), "Нет созданного item_id"
        item_id = self.__class__.created_item_id
        updated_data = {
            "title": "Обновленный заголовок",
            "description": "Новое описание"
        }

        response = auth_session.put(f"{self.endpoint}{item_id}", json=updated_data)
        assert response.status_code == 200, "Данные не обновились"

        data = response.json()
        assert data.get("title") == updated_data["title"]
        assert data.get("description") == updated_data["description"]

    def test_delete_item(self,auth_session):
        assert hasattr(self.__class__, "created_item_id"), "Нет созданного item_id"
        item_id = self.__class__.created_item_id

        response = auth_session.delete(f"{self.endpoint}{item_id}")
        assert response.status_code == 200, "Данные не удалились"

        get_response = auth_session.get(f"{self.endpoint}{item_id}")
        assert get_response.status_code == 404, "Элемент не удалён корректно"