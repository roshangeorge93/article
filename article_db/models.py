from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=30)
	author = models.CharField(max_length=30)
	pub_date = models.CharField(max_length=30)
	category = models.CharField(max_length=50)
	hero_image = models.CharField(max_length=50)
	opt_image = models.CharField(max_length=50)
	content = models.TextField()

#	def __unicode__(self):
#		return "hello sir"

