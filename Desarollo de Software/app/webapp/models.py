from django.db import models

# Create your models here.
class Thread(models.Model):
	title = models.CharField(max_length = 120)
	text = models.TextField(blank = True, null = True)
	username = models.CharField(max_length = 120, default = "Anonymous")
	createdAt = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f"/thread/{self.id}"

class Post(models.Model):
	text = models.TextField(blank = True, null = True)
	username = models.CharField(max_length = 120, default = "Anonymous")
	createdAt = models.DateTimeField(auto_now_add = True)
	thread_id = models.IntegerField()