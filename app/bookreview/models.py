from django.db import models

class UserManager(models.Manager):
    pass 

class User(models.Model):
    objects = UserManager()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    bank_account = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    bank_name = models.CharField(max_length=100)
    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.phone_number, self.bank_account, self.password, self.bank_name)


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


class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, related_name='books')

    def __unicode__(self):
        return self.title
