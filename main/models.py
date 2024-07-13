from django.db import models


class Kompany(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Ourservis(models.Model):
    service_name = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='ourservis_images/')

    def __str__(self):
        return self.service_name
    

class Aboutus(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='aboutus_images/')
    
    def __str__(self):
        return self.title
    

class Ourplans(models.Model):
    plan_name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.plan_name


class Ourteem(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ourteemp_images/')
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    messege = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    

