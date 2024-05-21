from django.db import models


class Location(models.Model):
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.description


class Department(models.Model):
    name = models.CharField(max_length=120)
    location = models.ForeignKey(Location, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)
    department = models.ForeignKey(Department, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
