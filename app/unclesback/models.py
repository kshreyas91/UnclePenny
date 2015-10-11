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
    currentsavings = models.CharField(max_length=100, default=0)
    futureestimate = models.CharField(max_length=100, default=0)
    currentChallenge = models.CharField(max_length=100, default="")
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

class ChallengeManager(models.Manager):
    pass


class Challenge(models.Model):
    objects = ChallengeManager()
    challenge_name = models.CharField(max_length=50)
    challenge_details = models.CharField(max_length=200)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    is_single = models.IntegerField(max_length=1)

    
class TeamManager(models.Manager):
    pass

class Team(models.Model):
    objects = TeamManager()
    team_name = models.CharField(max_length=200)
    challenge_id = models.CharField(max_length=200)#models.ForeignKey(Challenge,related_name='challenge_name')
    status = models.CharField(max_length=100, default="Yet to Begin!")

    def __unicode__(self):
        return '{} {}'.format(self.members,self.status)

class TeamMembersManager(models.Manager):
    pass

class TeamMembers(models.Model):
    objects = TeamMembersManager()
    userid = models.CharField(max_length=100)
    teamid = models.CharField(max_length=100)

    def __unicode__(self):
        return '{} {}'.format(self.userid,self.teamid)
    
class SingleChallegeMemebersManager(models.Manager):
    pass

class SingleChallegeMemebers(models.Model):
    objects = SingleChallegeMemebersManager()
    userid = models.CharField(max_length=100)
    challenge_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    def __unicode__(self):
        return '{} {}'.format(self.userid,self.challenge_name, self.status)
    

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
