from django.test import TestCase
from .models import Photographer,Photo,tags

class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Photographer(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Photographer))
    # Testing Save Method
    def test_save_method(self):
        self.james.save_photographer()
        photographer = Photographer.objects.all()
        self.assertTrue(len(photographer) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Photgrapher(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_Photgrapher()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_photo= Photo(title = 'Test Photo',post = 'This is a random test Post',editor = self.james)
        self.new_photo.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Photographer.objects.all().delete()
        tags.objects.all().delete()
        Photo.objects.all().delete()
    def test_get_pics_today(self):
        today_pics = Photo.todays_pics()
        self.assertTrue(len(today_pics)>0)