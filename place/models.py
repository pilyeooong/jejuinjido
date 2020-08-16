from django.db import models
from django.core.validators import RegexValidator


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     pass


class Place(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='places')
    name = models.CharField(max_length=30)
    description = models.TextField()
    address = models.TextField()
    website = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, blank=True)
    image = models.ImageField(upload_to='place/')
    lat = models.IntegerField()
    lng = models.IntegerField()
    congestion = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Congestion(TimeStampedModel):
    value = models.IntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='congestions')
