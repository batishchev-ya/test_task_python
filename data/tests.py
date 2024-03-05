from django.test import TestCase
from django.urls import reverse
import datetime

# Create your tests here.

class GetRequestTest(TestCase):
    def test_get_request(self):
        url = reverse('data')
        # url ='/data/'
        # print(url)
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        response = self.client.get(url, HTTP_ACCEPT_LANGUAGE='en', HTTP_USER_AGENT=user_agent)
        resonse_date=datetime.datetime.fromtimestamp(response.json()['ts']/1000)
        now_date=datetime.datetime.now()
        self.assertLess(resonse_date, now_date)