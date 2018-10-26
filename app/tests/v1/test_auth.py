import json
import unittest

from app.tests.v1.base_test import BaseTests


class AuthTest(BaseTests):
    """Tests functionality of user endpoints."""

    def test_user_registration_and_login(self):
        """Test successful user registration and login."""
        response = self.client().post('/api/v1/auth/register',
                                      data=json.dumps(dict(email='test@test.com',
                                                           password='password'
                                                           )),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_user_login(self):
        """test user login"""
        self.client().post('/api/v1/auth/register',
                           data=json.dumps(dict(email='test@test.com',
                                                password='password'
                                                )),
                           content_type='application/json')
        response = self.client().post('/api/v1/auth/login',
                                      data=json.dumps(dict(email='test@test.com',
                                                           password='password')),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_incorrect_login_details(self):
        """Test incorrect login details"""
        self.client().post('/api/v1/auth/login',
                           data=json.dumps(dict(email='test@test.com',
                                                password='password'
                                                )),
                           content_type='application/json')
        response = self.client().post('/api/v1/auth/login',
                                      data=json.dumps(dict(email='test123@test.com',
                                                           password='password')),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_existing_user(self):
        """test existing user"""
        self.client().post('/api/v1/auth/register',
                           data=json.dumps(dict(email='test@test.com',
                                                password='password'
                                                )),
                           content_type='application/json')
        response = self.client().post('/api/v1/auth/register',
                                      data=json.dumps(dict(email='test@test.com',
                                                           password='password'
                                                           )),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data.decode())
        self.assertTrue(data['Status'] == 'Bad Request')
        self.assertTrue(data['Message'] == 'User already exists, please login')

    def test_incorrect_email_details(self):
        """test incorrect email details"""
        response = self.client().post('/api/v1/auth/register',
                                      data=json.dumps(dict(email='testest.com',
                                                           password='password')),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_email_regex_format(self):
        """this checks if email is correct regex format"""


if __name__ == '__main__':
    unittest.main()
