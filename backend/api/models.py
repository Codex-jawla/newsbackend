from PIL import Image
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError


# Create your models here.

class Category(models.Model):
    cate_id=models.AutoField(primary_key=True)
    cate_name=models.TextField(max_length=100)

    def __str__(self):
        return self.cate_name

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Title=models.CharField(max_length=1000 ,default="")
    Slug = models.SlugField(max_length=1000,blank=True,editable=False)  # Add this line
    Content=RichTextField()
    Seo_Keyword=models.CharField(max_length=1000,default="")
    Seo_Title=models.CharField(max_length=1000,default="")
    Seo_Description = models.TextField(max_length=2000,default="")
    news_date=models.DateField(auto_now_add=True)
    Image=models.ImageField(upload_to='news_images/',default='news_images/default.jpeg')

    def save(self, *args, **kwargs):
        self.Slug = self.Title.replace(" ", "-")
        self.Slug= self.Slug.lower()
        self.Slug = slugify(self.Title)
        super().save(*args, **kwargs)

    def get_tags(self):
        return self.Seo_Keyword.split(" ")

    def __str__(self):
        return self.Title

    def clean(self):
        super().clean()
        # Validate the uploaded image
        if self.Image:
            image = Image.open(self.Image)

            # Validate dimensions
            max_width, max_height = 1920, 1080
            if image.width > max_width or image.height > max_height:
                raise ValidationError(
                    f"Image dimensions should not exceed {max_width}x{max_height}px. "
                    f"Uploaded image is {image.width}x{image.height}px."
                )

            # Validate format
            valid_formats = ["JPEG", "PNG"]
            if image.format not in valid_formats:
                raise ValidationError(f"Image format must be one of {valid_formats}. Uploaded format: {image.format}.")

