from django.test import TestCase

# Create your tests here.
import datetime

from .views import profile
from .models import Business, NeighbourHood, Post, Profile 
from django.contrib.auth.models import User
from django.test import TestCase

class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.profile = Profile(email='aa@gmail.com', photo='', bio='xxxx',
                                    user=self.user)
        self.profile.save()
        self.neighbourhood =  NeighbourHood(name = "Nairobi", location= "Ngara", admin = self.profile,description='xxxx', photo="")
        self.neighbourhood.save()
        
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)


class NeighbourHoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="tary", password="123")
        self.user.save()
        self.neighbourhood =  NeighbourHood(name = "Nairobi", location= "Ngara", admin = self.user,description='xxxx', photo="")
        self.neighbourhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,NeighbourHood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_neighbourhood()
        neighbourhood = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_neighbourhoodhood(self):
        self.neighbourhood.delete_neighbourhood()
        testsaved = NeighbourHood.objects.all()
        self.assertFalse(len(testsaved) > 0)
