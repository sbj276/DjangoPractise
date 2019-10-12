from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
	
	def testHomePage(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)
	
	def testAboutPage(self):
		response = self.client.get('/about/')
		self.assertEqual(response.status_code,200)


