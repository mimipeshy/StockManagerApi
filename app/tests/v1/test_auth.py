import json
import unittest

from app.tests.v1.base_test import BaseTests


class AuthTests(BaseTests):
    """Tests functionality of the auth endpoint"""

    def test_create_user(self):
        """Test API can create a user"""
        add_user= json.dumps({
            "email": "peris@gmail.com",
            "password":"South@frica1*"
        })
        response= self.client().post('/api/v1/auth/register',
                                    data=add_user,)

        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        """test API can login"""
        login_user= json.dumps({
            "email":"peris@gmail.com",
            "password":"South@frica1*"
        })
        response= self.client().post('/api/v1/auth/login',
                                     data= login_user
                                     )
        self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()