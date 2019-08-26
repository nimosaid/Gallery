from django.db import models
import datetime as dt


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    def save_Category(self):
        self.save()

class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    
    def save_photographer(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    photographer = models.ForeignKey(Photographer,on_delete=models.DO_NOTHING,)
    pub_date = models.DateTimeField(auto_now_add=True)
    Location = models.ForeignKey(Location,on_delete=models.DO_NOTHING,)
    Photos = models.ImageField(upload_to = 'photo/', blank=True)

    @classmethod
    def location(cls):
        pics = cls.objects.all()
        return pics

    @classmethod
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(category__icontains=search_term)
        return pics