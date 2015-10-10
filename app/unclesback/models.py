from django.db import models

class UserProfileManager(models.Manager):
    pass 

class UserProfile(models.Model):
    objects = UserProfileManager()
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=12)
    banknumber = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    bankname = models.CharField(max_length=100)
    def __unicode__(self):
        return '{} {}'.format(self.firstname, self.lastname, self.username, self.banknumber, self.password, self.bankname)


class AuthorManager(models.Manager):
    pass


class Author(models.Model):
    objects = AuthorManager()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class BookManager(models.Manager):
    pass


class StatusObjectManager(models.Manager):
    pass 

class StatusObject(models.Model):
    objects = StatusObjectManager()
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return '{} {}'.format(self.status, self.message)

class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, related_name='books')

    def __unicode__(self):
        return self.title
