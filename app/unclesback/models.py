from django.db import models
from listField import ListField

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
    currentsavings = models.DecimalField(max_digits=10,decimal_places = 2)
    futureestimate = models.DecimalField(max_digits=10,decimal_places = 2)

    def __unicode__(self):
        return '{} {}'.format(self.firstname, self.lastname, self.username, self.banknumber, self.password, self.bankname,self.currentsavings,self.futureestimate)

class StatusObjectManager(models.Manager):
    pass 

class StatusObject(models.Model):
    objects = StatusObjectManager()
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return '{} {}'.format(self.status, self.message)


# class AuthorManager(models.Manager):
#     pass


# class Author(models.Model):
#     objects = AuthorManager()
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)

#     def __unicode__(self):
#         return '{} {}'.format(self.first_name, self.last_name)

class ChallengeManager(models.Manager):
    pass


class Challenge(models.Manager):
    objects = ChallengeManager()
    challenge_name = models.CharField(max_length=50)
    challenge_details = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    def __unicode__(self):
        return '{} {}'.format(self.challenge_name, challenge_details, self.start_date, self.end_date)


class TeamManager(models.Manager):
    pass

class Team(models.Model):
    objects = TeamManager()
    members = ListField()#a list of names (could be (name,id) as well--undecided) of members who are participating
    challenge_name = models.CharField(max_length=200)#models.ForeignKey(Challenge,related_name='challenge_name')
    status = models.DecimalField(max_digits=5,decimal_places = 2)

    def __unicode__(self):
        return '{} {}'.format(self.members,self.status)


class ActivityFeedManager(models.Manager):
    pass

class ActivityFeed(models.Model):
    objects = ActivityFeedManager()


# class Book(models.Model):
#     objects = BookManager()
#     title = models.CharField(max_length=200)
#     isbn = models.CharField(max_length=20)
#     author = models.ForeignKey(Author, related_name='books')

    # def __unicode__(self):
    #     return self.title
