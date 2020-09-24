from django.db import models
from django.contrib.auth.models import User

class Topic( models.Model):
    '''A topic the user is learning about '''
    #store the text representing the topic
    text = models.CharField(max_length=200) 
    
    #record the date and time the entry was created ( auto_now_add argument
    # tells django to fill this field automatically. )
    date_added= models.DateTimeField( auto_now_add = True)
    
    #attribute each topic to unique users i.e every user has access to only their topics
    owner = models.ForeignKey(User, on_delete = models.CASCADE)


    def __str__(self):
        '''Return a string representation of the model. '''
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    # create a relationship between Entry and Topic.
    # Many Entries can have one topic : Many-to-one relationship.
    # models.CASCADE argument makes django to delete all entries associated 
    # to a topic once the topic is deleted. => a.k.a cascading delete
    topic = models.ForeignKey( Topic, on_delete= models.CASCADE)

    text = models.TextField() #content of the entry
    #record the date and time the entry was created ( auto_now_add argument
    # tells django to fill this field automatically. )
    date_added = models.DateTimeField( auto_now_add = True )

    #holds extra information for managing Entry model.
    #verbose_name_plural simply tells django to use 'Entries' when referring
    #to more than one entry. Otherwise django would use 'Entrys'.
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


