import os
import sys
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) + "/src/app"
sys.path.insert(0, parent)

from app import app


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.context.pop()
        self.app = None
        self.context = None

    def test_app(self):
        assert self.app is not None
        assert app == self.app

    def test_main(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_user_athentication_and_notes(self):
        response = self.client.post(
            "/sign_up", data={"name": "test_name", "password": "test_password"}
        )
        assert (
            """URL: <a href="/notes/test_name">/notes/test_name</a>"""
            in response.get_data(as_text=True)
        )

        response = self.client.post(
            "/log_in", data={"name": "test_name", "password": "test_password"}
        )
        assert (
            """URL: <a href="/notes/test_name">/notes/test_name</a>"""
            in response.get_data(as_text=True)
        )

        response = self.client.get("/notes/test_name")
        assert "Add a note" in response.get_data(
            as_text=True
        ) and "List the notes" in response.get_data(as_text=True)

        response = self.client.post(
            "/add_notes/test_name", data={"title": "test_title", "text": "test_text"}
        )
        assert (
            """URL: <a href="/notes/test_name">/notes/test_name</a>"""
            in response.get_data(as_text=True)
        )

        response = self.client.get("/list_notes/test_name")
        assert (
            """{"1":{"text":"test_text","title":"test_title","username":"test_name"}}"""
            in response.get_data(as_text=True)
        )

        response = self.client.get("/users")
        assert """{"test_name":"test_password"}""" in response.get_data(as_text=True)


if __name__ == "__main__":
    unittest.main()
