from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

    def __str__(self):
        return "- ( id: " + str(self.id) + ", dojo name: " + self.name + ", dojo city: " + self.city + ", dojo state: " + self.state + " ) -"

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name='ninjas')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "- ( id: " + str(self.id) + ", ninja first name: " + self.first_name + ", ninja last name: " + self.last_name + " ) -"