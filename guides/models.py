from django.db import models


class Guide(models.Model):

    title  = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    language = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    price = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='uploads/')


    def __str__(self):
        return self.title
