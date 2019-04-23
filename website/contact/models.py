from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	email = models.EmailField()
	message = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return ('%s | %s')%(self.email, self.subject)
