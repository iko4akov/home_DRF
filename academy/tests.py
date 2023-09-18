import os

from rest_framework import status
from rest_framework.test import APITestCase

from academy.models import Lesson
from user.management.commands.fill_users import Command
from user.models import User


class HeadersMixin:

    def get_headers(self):
        """Create user for test"""
        com = Command()
        com.handle()
        user = {
            'email': '2@2.com',
            'password': '2@2.com'
        }

        access_token = self.client.post('/user/token/', data=user).json().get('access')
        token = 'Bearer ' + access_token

        headers = {'Authorization': token}

        return headers

class AcademyTestCase(APITestCase, HeadersMixin):
    headers = None

    def setUp(self) -> None:
        self.headers = self.get_headers()
        Lesson.objects.create(name='test1', description='test1descr1', owner=User.objects.get(pk=2))

    def test_create_lesson(self):
        """Test case 1 create lesson"""

        data = {
            'name': 'test2',
            'description': '2',
            'owner': 2
        }

        respounse = self.client.post(
            '/lesson/create/',
            data=data,
            headers=self.headers
        )

        self.assertEqual(
            respounse.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            respounse.json().get('name'),
            data.get('name')
        )

        self.assertTrue(
            Lesson.objects.get(pk=2).name,
            data.get('name')
        )


    def test_delete_lesson(self):
        """Test Case delete lesson"""


        respounse = self.client.delete(
            '/lesson/delete/3/',
            headers=self.headers
        )

        self.assertEqual(
            respounse.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.all().exists()
        )


    def test_list_lesson(self):
        """test case listlesson"""

        respounse = self.client.get(
            '/lesson/',
            headers=self.headers
        )
        self.assertEqual(
            respounse.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            Lesson.objects.get(pk=4).name,
            respounse.json().get('results')[0].get('name')
        )

    def test_update_lesson(self):
        """Test case update lesson"""


        data = {
            'name': 'testupdate',
            'description': 'test1descrupdate'
        }

        respounse = self.client.patch(
            '/lesson/update/5/',
            data=data,
            headers=self.headers
        )

        self.assertEqual(
            respounse.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data.get('name'),
            respounse.json().get('name')
        )

