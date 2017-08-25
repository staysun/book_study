from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)



class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2,default=10)
    authors=models.ManyToManyField("Author")

    publisher = models.ForeignKey(Publisher)  #  数据库存的publisher_id

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Book2Author(models.Model):
      author = models.ForeignKey("Author")
      Book = models.ForeignKey("Book")