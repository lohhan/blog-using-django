from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
   caption = models.CharField(max_length=20)

   def __str__(self):
      return f"{self.caption}"

class Author(models.Model):
   first_name = models.CharField(max_length=80)
   last_name = models.CharField(max_length=80)
   email_adress = models.EmailField()

   def __str__(self):
      return f"{self.first_name} {self.last_name}"

class Post(models.Model):
   title = models.CharField(max_length=150)
   author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
   excerpt = models.CharField(max_length=200)
   image_name = models.CharField(max_length=100)
   date = models.DateField(auto_now=True)
   slug = models.SlugField(null=True, blank=True, unique=True)
   content = models.TextField(validators=[MinLengthValidator(10)])
   tag = models.ManyToManyField(Tag, related_name="posts")

   def save(self, *args, **kwargs):
      self.slug = slugify(self.title,)
      super().save(*args, **kwargs)

   def __str__(self):
      return f"{self.title}"


   
