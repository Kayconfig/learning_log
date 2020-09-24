from django.shortcuts import render,HttpResponse, redirect
from learning_logs.models import Topic, Entry
from learning_logs.forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


#homepage
def index(request):
    '''The home page for Learning Log.'''
    return render( request, 'learning_logs/index.html')

# restrict access
@login_required
def topics( request):
    '''show all topics '''
    # query the database for topics and sort by the date_added attribute, 
    # restricting topics access to appropriate Users.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # a dictionary in which keys are names I used in the template to access data
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''show a single topic and all its entries.'''
    topic = Topic.objects.get(id=topic_id)
    
    #Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        return redirect('learning_logs:topics')

    # the '-' in front of the date_added argument, makes django to 
    # sort the entries by reverse order( latest to earliest )
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    ''' adds a new topic '''
    if request.method != 'POST':
        #no data was submitted, create a blank form
        form = TopicForm()
    else:
        #data was submitted save new topic
        form = TopicForm(request.POST)
        if form.is_valid():
            #Associate new topics with the current user
            newTopic = form.save( commit=False)
            newTopic.owner = request.user
            newTopic.save()
            return redirect('learning_logs:topics')
    
    #display blank form or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''Add a new entry to the topic with id == topic_id'''
    #get the topic
    topic = Topic.objects.get(id= topic_id)
    if topic.owner != request.user:
        return redirect('learning_logs:topics')
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

@login_required
def edit_entry( request, entry_id):
    '''Edit an existing entry'''
    entry = Entry.objects.get(id= entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        return redirect('learning_logs:topics')

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


@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.user == topic.owner:#only topic owners can delete topic
        action = request.GET['action']
        if action == "confirm": #confirm if the user wants to delete
            context = {'topic': topic}
            return render(request, 'learning_logs/confirmDelete.html', context)
        elif action == "delete": #the user has confirmed the delete action
            topic.delete()

    #return to topics
    return redirect('learning_logs:topics')

@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get( id=entry_id)
    topic = entry.topic
    if request.user != topic.owner: #if user is not the owner
        return redirect('learning_logs:topics')
    else: # user is the owner
        entry.delete()
        return redirect('learning_logs:topic', topic_id= topic.id)
    
        



