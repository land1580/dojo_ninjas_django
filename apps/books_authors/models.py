from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "- ( id: " + str(self.id) + ", book name: " + self.name + ", book description: " + self.desc + " ) -"

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    books = models.ManyToManyField(Book, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    

    def __str__(self):
        return "- ( id: " + str(self.id) + ", author 1st name: " + self.first_name + ", author last name: " + self.last_name + ", author email: " + self.email + ", books: " + " ) -"
