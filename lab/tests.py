from django.test import TestCase

# Create your tests here.
"""testing module for the tickets app"""

from django.test import TestCase, Client
from users.models import User
from .models import Team
from priority.models import Clients


class TeamTest(TestCase):
    """Testing class for Teams"""

    def setUp(self):
        """This runs at start of test, creates a user and a client"""
        self.client = Client()
        user = User.objects.create(username='Maartin', password='vandeBurg')
        self.ticket = Clients.objects.create(user=user, department='bug', project='big bug', supervisor='bug')

#    def test_ticket_model_create(self):
#        """Testing function for ticket creation form"""
#        user_name = User.objects.create(username='Fred2', password='freddie')
#        ticket = Ticket.objects.create(author=user_name, title='feature', text='big feature')
#        assert len(Ticket.objects.all()) == 2
#
    def test_view(self):
        """This checks the tickets view page has loaded correctly"""
        res = self.client.get('/lab/')
        assert b'request' in res.content

