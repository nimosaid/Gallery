from django.db import models

class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    
    def save_photographer(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    photographer = models.ForeignKey(Photographer,on_delete=models.DO_NOTHING,)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def days_pics(cls,date):
        pics = cls.objects.filter(pub_date__date = date)
        return pics
    @classmethod
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics