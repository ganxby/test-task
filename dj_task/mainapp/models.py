from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 128)
    username = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)
    phone = models.CharField(max_length = 128)
    website = models.CharField(max_length = 128)


    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length = 128)
    suite = models.CharField(max_length = 128)
    city = models.CharField(max_length = 128)
    zipcode = models.CharField(max_length = 128)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return (self.street + ' --> ' + str(self.user))

class Geo(models.Model):
    latitude = models.CharField(max_length = 128)
    longitude = models.CharField(max_length = 128)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)

    def __str__(self):
        return (self.latitude + ', ' + self.longitude + ' --> ' + str(self.address))

class Company(models.Model):
    name = models.CharField(max_length = 128)
    catchPhrase = models.CharField(max_length = 128)
    bs = models.CharField(max_length = 128)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return (self.name + ' --> ' + str(self.user))

################ different type of models ################

class Post(models.Model):
    title = models.CharField(max_length = 128)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return (self.title + ' --> ' + str(self.user))

