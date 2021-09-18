from unittest import TestCase
from unittest.mock import patch
from page import PageRequester


class Test_Request(TestCase):
    def setUp(self):
        self.page = PageRequester("https://google.com")

    def test_request(self):
        with patch("requests.get") as mocked:
            self.page.get()
            mocked.assert_called()

    def test_content(self):
        fake_content = "hello, world "

        class fake_response:
            def __init__(self):
                self.content = fake_content

        with patch("requests.get", return_value=fake_response()):
            result = self.page.get()
            self.assertEqual(result, fake_content)
