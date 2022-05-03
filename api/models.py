from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(default='')
    city = models.CharField(max_length=45)
    address = models.TextField(default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }

class People(models.Model):
    name = models.CharField(max_length=35)
    age = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

class Products(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    price = models.IntegerField()
    person = models.ForeignKey(People, on_delete=models.CASCADE, null=True)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

