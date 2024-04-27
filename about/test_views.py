from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm




class TestAboutView(TestCase):

    # def test_page_loads_correctly(self):
    #     about_form = CollaborateForm({'name':'george', 'email':'tester@hotmal.co.uk','message': 'This is a great post'})
    #     self.assertTrue(about_form.is_valid(), msg='Form is not valid')
    def setUp(self):
        
        self.about_content = About(title="about-me", 
                         content="this is the body of the about")
        self.about_content.save()
        
    def test_page_loads_correctly(self):
        response = self.client.get(reverse(
            'about'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"about-me", response.content)
        self.assertIn(b"this is the body of the about", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
        
    def test_successful_submission_of_a_collaboration_request(self):
        form = {
            'name': 'Matt',
            'email': 'test@test.com',
            'message': 'testing 123',
        }
        response = self.client.post(reverse(
            'about'), form)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )


