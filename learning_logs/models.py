from django.db import models

class Topic( models.Model):
    '''A topic the user is learning about '''
    #store the text representing the topic
    text = models.CharField(max_length=200) 

    #record date and time the topic was created( auto_now_add argument
    # tells django to automatically set this attribute to the current
    # date and time whenever the user creates a new topic)
    date_added= models.DateTimeField( auto_now_add = True)
    

    def __str__(self):
        '''Return a string representation of the model. '''
        return self.text
