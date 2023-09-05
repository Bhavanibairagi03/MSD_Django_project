from django.db import models

# Create your models here.
class Geeks(models.Model):
    title=models.CharField(max_length=200)
    discription=models.TextField()
    last_modified=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to="myimage")
    def __str__(self):
        return self.title
