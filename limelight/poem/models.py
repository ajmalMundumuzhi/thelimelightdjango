from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Poem(models.Model):
    LIVE = 1 
    DELETE = 0
    DELETE_CHOICE = (
        (LIVE,'Live'),
        (DELETE,'Delete')
    )

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    institution = models.CharField(max_length=300)
    description = models.TextField()
    detail = HTMLField()  
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    delete_choice = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
