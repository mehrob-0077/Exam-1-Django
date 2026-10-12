from django.db import models


class Ganr(models.Model):
    name = models.CharField(max_length=100)
    kino = models.ForeignKey("Kino",on_delete=models.CASCADE,related_name="kino")

    def __str__(self):
        return self.name



class Kino(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    time = models.DateTimeField()
    price = models.IntegerField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='menu_images/')


    def __str__(self):
        return self.title





class Feedback(models.Model):
    message = models.TextField() 



