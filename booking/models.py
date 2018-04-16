from django.db import models

# Create your models here.
# class Event(models.Model):
#     event_name = models.TextField(max_length=200, unique=True, default='')
#
#     def __str__(self):
#         return '%s' % (self.event_name)
#
# class Date(models.Model):
#     event = models.ForeignKey(event_name,on_delete=models.CASCADE)
#     date = models.DateField(auto_now=False)
#
#     def __str__(self):
#         return '%s' % (self.sub_category)
