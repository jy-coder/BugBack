from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from database.models import Bug
from database.serializers import BugSerializer
from knox.models import AuthToken

class BaseTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('johnny', email='jb@gmail.com', password='j54321')
        self.user2 = User.objects.create_user('kelvin', email='kc@gmail.com', password='k54321')
        self.user.save()
        self.token = AuthToken.objects.create(self.user)[1]

        # client authenticate with user
        self.client = APIClient()
        self.client.login(username=self.user.username, password='j54321')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        self.addbug_url = reverse('addbugrpt')
        self.datas = Bug.objects.create(name='apitestcase new bug', status='new',
                                   description='this is some apitestcase bug i found at patch ver 2.01',
                                   priority='low', reported_by=self.user2, developer_assigned=self.user)

        # test serializer with bug object
        self.bug_serializer = BugSerializer(self.datas)
        self.response = self.client.post(self.addbug_url, self.bug_serializer.data, format='json')

        return super().setUp()

class SearchTest(BaseTest):
    def test_can_access_search_bug(self):
        searchbug_url = '/bug/search/?q='
        response2 = self.client.get(searchbug_url, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        print("Able to access search view-name success!")
        print()

    def test_can_search_bug_name(self):
        # test search bug with query bug name 'apitestcase'
        search_url = '/bug/search/?q=apitestcase'
        response2 = self.client.get(search_url, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

        print("Response data: ", end=" ")
        print(response2.data[0])

        # test data retrieved based on search query is correct
        self.assertEqual(response2.data[0], self.bug_serializer.data)
        print("Able to search bug correctly success!")
        print()

    def test_can_search_bug_assignee(self):
        # test search bug with query assignee username 'kelvin'
        search_url = '/bug/assign_search/?q=kelvin'
        response2 = self.client.get(search_url, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        print("Able to access search view-assignee success!")

        print("Search by assignee data: ", end=" ")
        print(response2.data[0])

        # test data retrieved based on search query is correct
        self.assertEqual(response2.data[0], self.bug_serializer.data)
        print("Able to search bug assignee correctly success!")
        print()