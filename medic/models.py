from django.db import models
from django.utils import timezone
# Create your models here.
class medicine(models.Model):
    device_id = models.ForeignKey('device', on_delete=models.CASCADE)
    med_name = models.CharField(max_length=200)
    med_no = models.IntegerField()
    morning = models.IntegerField()
    afternoon = models.IntegerField()
    evening = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.med_name

class device(models.Model):
	name=models.CharField(max_length=200)
	devid=models.IntegerField();


	def __str__(self):
		return self.name