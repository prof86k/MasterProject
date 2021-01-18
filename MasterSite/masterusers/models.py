from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
# ++++++++++++++++++++++++++++++++ user learns models here +++++++++++++++++++++++++++++++++++++++= 

class Subject(models.Model):
    """ A subject taken by a user"""
    # User models as a foreign key to this model
    name = models.CharField("Subject Name:",max_length=25,null=False,blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    """ Top learned by the user """
    # Subject model as a foreign key to this model
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    topic_name = models.CharField("Topic Name",max_length=25,null=False,blank=False)
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic_name



class Learn(models.Model):
    """ learns of the day can be saved into user account through subject"""
    # topic model as a foriegn key to this model
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    lession_type = models.CharField(max_length=24,null=False,blank=False)
    lession = RichTextUploadingField(null=True,blank=True,config_name='special')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.lession_type