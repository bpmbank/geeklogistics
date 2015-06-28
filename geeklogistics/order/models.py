from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=30)
    deliver_id = models.CharField(max_length=50)
    poi_id = models.CharField(max_length=30)
    current_location = models.CharField(max_length=60)
    ctime = models.DateField(max_length=30)
    utime = models.DateField(max_length=30)
    status = models.CharField(max_length=3)

    def __unicode__(self):
        return self.order_id