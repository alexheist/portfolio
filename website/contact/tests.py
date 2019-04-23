from django.urls import revers
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Contact
from .serializers import ContactSerializer

class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def submit_contact(name='', subject='', phone='', email='', message=''):
		if name != '' and subject != '' and phone != '' and email != '':
			Contact.objects.create(
				name = name,
				subject = subject, 
				phone = phone,
				email = email,
				message = message,
			)
			
	def setUp(self):
		self.submit_contact('Mom', 'How are you', '1234567890', 'mom@email.com')
		self.submit_contact('Dad', 'Proud of you', '3215123892', 'dad@email.com', 'Additional Text')
		self.submit_contact('Sister', 'Ugh', '2348925923', 'sister@email.com')
		self.submit_inquiry('Brother', 'yo', '2347235123', 'brother@email.com')

class GetAllContact(BaseViewTest):
	def test_get_contact(self):
		response = self.client.get(
			reverse(
				'contact-all', 
				kwargs = {
					'version': 'v1'
				}
			)
		)
		expected = Contact.objects.all()
		serialized = ContactSerializer(expected, many=True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
