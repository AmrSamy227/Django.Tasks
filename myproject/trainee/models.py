from django.db import models
from track.models import Track
# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.BooleanField(default=True)
    trackid = models.ForeignKey(Track, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='trainee_photos/', null=True, blank=True)

    @classmethod
    def getalltrainee(cls):
        return cls.objects.filter(status=True)

    @classmethod
    def gettraineeByid(cls, id):
        return cls.objects.get(id=id)
