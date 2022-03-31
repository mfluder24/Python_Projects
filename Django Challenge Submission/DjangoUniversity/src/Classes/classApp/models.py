from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=60)
    Duration = models.DecimalField(max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.Title