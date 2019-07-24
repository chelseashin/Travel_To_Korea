from django.db import models
from accounts.models import MyUser

# Create your models here.
class Common(models.Model):
    contentId = models.IntegerField(unique=True, primary_key=True)
    sigungu = models.IntegerField()
    area = models.IntegerField()
    category = models.IntegerField()
    title = models.TextField()
    tel = models.TextField()
    overview = models.TextField()
    addr1 = models.TextField()
    addr2 = models.TextField()
    homepage = models.TextField()
    avgScore = models.FloatField()
    zipCode = models.IntegerField()
    image = models.TextField()

    def __str__(self):
       return self.title

class Detail(models.Model):
    detailId = models.ForeignKey(Common, on_delete=models.CASCADE)
    startTime = models.TextField()
    endTime = models.TextField()
    parking = models.TextField()
    chkPet = models.TextField()
    chkBaby = models.TextField()
    age =  models.TextField()
    pay = models.TextField()
    barbeque = models.TextField()
    refund = models.TextField()

class Bookmark(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, primary_key=True)
    inform = models.ForeignKey(Common, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "inform")


class Stamp(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, primary_key=True)
    inform = models.ForeignKey(Common, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "inform")

class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, primary_key=True)
    inform = models.ForeignKey(Common, on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
       return (self.user, self.content)

    class Meta:
        unique_together = ("user", "inform")

class Score(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, primary_key=True)
    inform = models.ForeignKey(Common, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
       return (self.user, self.score)

    class Meta:
        unique_together = ("user", "inform")