from django.db import models

# Create your models here.


class Projects(models.Model):
    choice = (('NEW', "NEW"), ("OLD", "OLD"))
    project_name = models.CharField(max_length=100)
    project_image = models.ImageField()
    project_des = models.TextField(blank=True, null=True)
    project_link = models.CharField(max_length=300)
    project_code_link = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(choices=choice, max_length=4)

    def __str__(self):
        return self.project_name


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_image = models.ImageField()

    def __str__(self):
        return self.certificate_name
