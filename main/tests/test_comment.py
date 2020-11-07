from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from accounts.serializers import UserSerializer
from database.models import Bug, Comment
from database.serializers import BugSerializer, CommentSerializer
from knox.models import AuthToken

class BaseTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('johnny', email='jb@gmail.com', password='j54321')
        self.user.save()
        #second user for reporting bug
        self.user2 = User.objects.create_user('howard', email='dhow@gmail.com', password='d54321')
        self.user2.save()
        self.token = AuthToken.objects.create(self.user)[1]

        # client authenticate with user
        self.client = APIClient()
        self.client.login(username=self.user.username, password='j54321')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # bug dummy data for test
        self.addbug_url = reverse('addbugrpt')
        self.bug_data = Bug.objects.create(name='testunit comment bug', status='new',
                                   description='this is some testunit bug on patch ver 3.51',
                                   priority='medium',reported_by=self.user, developer_assigned=self.user)

        self.bug_serializer = BugSerializer(self.bug_data)
        #self.bugid = self.bug_serializer.save()
        self.response = self.client.post(self.addbug_url, self.bug_serializer.data, format='json')

        return super().setUp()

class CommentTest(BaseTest):
    def test_can_add_comment(self):
        # test access comment/1/ from CommentAPI view after adding a bug id=1
        addcomment_url = reverse('comment', args=(self.bug_data.id,))

        # add comment to a bug
        comment_data = Comment.objects.create(comment_text='i do have this bug too! Any solution?', user=self.user,
                                   bug_id=self.bug_data.id)

        # test serializer with Comment object
        comment_serializer = CommentSerializer(comment_data)
        response = self.client.post(addcomment_url, comment_serializer.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Response comment data: ", end=" ")
        print(comment_serializer.data)
        print("Add Comment Success!")
        print()

    def test_can_get_comment(self):
        # test access comment/1/ from CommentAPI view when adding a bug id=1
        addcomment_url = reverse('comment', args=(self.bug_data.id,))

        # add comment to a bug
        comment_data = Comment.objects.create(comment_text='i do have this bug too! Any solution?', user=self.user,
                                              bug_id=self.bug_data.id)

        # test serializer with Comment object
        comment_serializer = CommentSerializer(comment_data)
        response = self.client.post(addcomment_url, comment_serializer.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # test access comment/1/ from CommentAPI view after adding a bug id=1
        viewcomment_url = reverse('comment', args=(self.bug_data.id,))
        response2 = self.client.get(viewcomment_url, format='json')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        print("Access Added Comment View to Bug Success!")

        print("Response data: ", end=" ")
        print(response2.data[0])
        # test data GET from CommentAPI is same as the data POST previously to the bug report
        self.assertEqual(response2.data[0], comment_serializer.data)
        print("View newly Added comment Success!")
        self.client.logout()
        print()


