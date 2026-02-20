from django.db import models


class SubscriberEmail(models.Model):
	subscriber_id = models.AutoField(primary_key=True)
	subscriber_email = models.EmailField(max_length=100, default=None)
	date_joined = models.DateField(auto_now_add=True)

