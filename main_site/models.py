from django.db import models


class ResourceLink(models.Model):
    COURSE_CHOICES = (
    ('GEN', 'General'),
    ('FOMB', 'Foundations of Modern Biology'),
    ('CBB', 'Cell Biology and Biochemistry'),
    ('MLBA', "Machine Learning for Biomedical Applications"),
    ('ACB', 'Algorithms in Computational Biology'),
    ('NB', 'Network Biology'),
    ('CGAS', 'Computational Gastronomy'),
    ('IMB', 'Introduction to Mathematical Biology'),
    )
    name = models.CharField(max_length=250)
    link = models.URLField(max_length=300)
    description = models.TextField(max_length=300, default='')
    contributor = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=250, choices=COURSE_CHOICES, default='GEN')


    def __str__(self):
        return self.name
