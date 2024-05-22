from django.contrib.auth.models import User
from rest_framework import status
from store.models import Collection, Product
import pytest
from model_bakery import baker

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection

class TestCreateCollection:
    @pytest.mark.django_db
    # @pytest.mark.skip #to skip the test
    def test_if_user_is_anonymous_return_401(self, create_collection):
        # AAA (Arrange, Act, Assert)
        # Arrange

        # Act
        response = create_collection({'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_if_user_is_not_admin_return_403(self, authenticate, create_collection):
        authenticate()

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, authenticate, create_collection):
        authenticate(is_staff=True)
        # api_client.force_authenticate(user=User(is_staff=True))

        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
    
    @pytest.mark.django_db
    def test_if_data_is_valid_return_201(self, authenticate, create_collection):
        authenticate(is_staff=True)
        # api_client.force_authenticate(user=User(is_staff=True))

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

class TestRetrieveCollection:

    @pytest.mark.django_db
    def test_if_collection_exists_return_200(self, api_client):
        # Arrange
        collection = baker.make(Collection)
        # breakpoint()
        # baker.make(Product, collection=collection, _quantity=10)

        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == collection.id
        assert response.data['title'] == collection.title
        # assert response.data == {
        #     'id' : collection.id,
        #     # 'title' : collection.title,
        #     # 'product_count' : 0
        # }


