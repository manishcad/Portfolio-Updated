from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Projects(models.Model):
    choice = (('NEW', "NEW"), ("OLD", "OLD"))
    project_name = models.CharField(max_length=100)
    project_image = models.ImageField()
    project_des = models.TextField(blank=True, null=True)
    project_link = models.CharField(max_length=300)
    project_code_link = models.CharField(max_length=300, blank=True, null=True)
    total_up_vote = models.IntegerField(default=0, blank=True, null=True)
    total_down_vote = models.IntegerField(default=0, blank=True, null=True)
    status = models.CharField(choices=choice, max_length=4)
    tags = models.ManyToManyField('Tag', blank=True, null=True)

    def __str__(self):
        return self.project_name


class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_image = models.ImageField()

    def __str__(self):
        return self.certificate_name


class Review(models.Model):
    choice = (('Up', 'Up Vote'), ('Down', 'Down Vote'))
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.CharField(max_length=20, choices=choice)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.vote


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
