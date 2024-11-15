from django.db import models

class noticedb(models.Model):
    noticeId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    contents = models.TextField()
    writeDate = models.DateTimeField(auto_now_add=True)
    publishDate = models.DateTimeField()
    expiryDate = models.DateTimeField()
    publishType = models.CharField(max_length=1)
    pushType = models.CharField(max_length=1)

    def __str__(self):
        return self.title