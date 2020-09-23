from django.shortcuts import render,HttpResponse
from learning_logs.models import Topic, Entry


#homepage
def index(request):
    '''The home page for Learning Log.'''
    return render( request, 'learning_logs/index.html')

def topics( request):
    '''show all topics '''
    # query the database for topics and sort by the date_added attribute
    topics = Topic.objects.order_by('date_added')
    # a dictionary in which keys are names I used in the template to access data
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''show a single topic and all its entries.'''
    topic = Topic.objects.get(id=topic_id)
    # the '-' in front of the date_added argument, makes django to 
    # sort the entries by reverse order( latest to earliest )
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)
