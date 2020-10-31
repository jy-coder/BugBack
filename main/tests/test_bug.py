from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from accounts.serializers import UserSerializer
from database.models import Bug, Comment
from database.serializers import BugSerializer, BugReportSerializer
from model_bakery import baker
from knox.models import AuthToken

class BaseTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('johnny', email='jb@gmail.com', password='j54321')
        self.user.save()
        self.token = AuthToken.objects.create(self.user)[1]

        # client authenticate with user
        self.client = APIClient()
        self.client.login(username=self.user.username, password='j54321')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        return super().setUp()

class BugTest(BaseTest):
    def test_can_add_bug(self):
        addbug_url = reverse('addbugrpt')

        # data = {"name": "testunit new bug", "status": "new",
        #         "description": "this is some testunit bug i found at patch ver 1.01",
        #         "priority": "", "upvote_count": 0, "downvote_count": 0, "created_at": "2020-10-30T09:04:30.477007Z",
        #         "updated_at": "2020-10-30T09:04:30.477007Z", "reported_by": 7, "developer_assigned": "", "comment": "",
        #         }

        # create bug object with dummy data
        datas = Bug.objects.create(name='testunit new bug', status='new',
                                   description='this is some testunit bug i found at patch ver 1.01',
                                   priority='high',reported_by=self.user, developer_assigned=self.user,
                                   comment=Comment.objects.create(comment_text="hello test"))

        # test serializer with bug object
        bug_serializer = BugReportSerializer(datas)
        response = self.client.post(addbug_url, bug_serializer.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Add Bug Success!")

        # test access bugreport/1/ from BugReportAPI view after adding a bug id=1
        id = 1
        viewbug_url = reverse('bugrpt', args=(id,))
        response2 = self.client.get(viewbug_url)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        print("Access Added Bug View Success!")

        # print(response2.json())
        # test data retrieved from BugReportAPI is same as the data POST from AddBugReportAPI
        self.assertEqual(response2.json(), bug_serializer.data)
        print("View newly Added Bug Success!")
        self.client.logout()
