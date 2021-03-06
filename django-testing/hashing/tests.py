from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import Hash
class UnitTestCase(TestCase):
    def test_home_homepage_tempalte(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')
    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())
    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)
    def test_hash_object(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()
        pulled_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(hash.text, pulled_hash.text)

        
# class FunctionalTestCase(TestCase):
    
#     def setUp(self):
#         self.browser = webdriver.Chrome()
        
#     def tearDown(self):
#         self.browser.quit()
        
#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter hash here',self.browser.page_source)
        
#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000')
#          # Find the element with id "text"
#         text = self.browser.find_element_by_id("id_text")
#         text.send_keys("Hello")
#         self.browser.find_element_by_name("submit").click()
#         # Result must be the correct walue
#         self.assertInHTML('185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969', self.browser.page_source)