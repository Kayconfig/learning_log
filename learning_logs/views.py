from django.shortcuts import render,HttpResponse, redirect
from learning_logs.models import Topic, Entry
from learning_logs.forms import TopicForm, EntryForm


#homepage
def index(request):
    '''The home page for Learning Log.'''
    if request.user.is_authenticated:
        return render( request, 'learning_logs/index.html')
    else:
        return redirect('users:login')

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

def new_topic(request):
    ''' adds a new topic '''
    if request.method != 'POST':
        #no data was submitted, create a blank form
        form = TopicForm()
    else:
        #data was submitted save new topic
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    #display blank form or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    '''Add a new entry to the topic with id == topic_id'''
    #get the topic
    topic = Topic.objects.get(id= topic_id)
    if request.method != 'POST':
        #no data was submitted create empty form
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            #dont add the entry to the database yet
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    #display a blank or invalid form
    context = {'topic':topic, 'form':form}
    return render( request, 'learning_logs/new_entry.html', context)


def edit_entry( request, entry_id):
    '''Edit an existing entry'''
    entry = Entry.objects.get(id= entry_id)
    topic = entry.topic

    if request.method != "POST":
        #no data was submitted, fill the form with current data.
        form = EntryForm(instance=entry)
    else:
        #data was submitted, update the entry
        form =  EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            #the content of the form is valid
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    context = {'entry':entry, 'form':form, 'topic':topic}
    return render( request, 'learning_logs/edit_entry.html', context)


