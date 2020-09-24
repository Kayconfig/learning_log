from django import forms
from learning_logs.models import Topic, Entry

class TopicForm( forms.ModelForm):
    class Meta:
        model = Topic # tells django which model to base the form on
        fields = ['text']
        labels = {'text': ''} # tells django not to generate a label for the text field


class EntryForm( forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        widgets= {'text': forms.Textarea(attrs = {'cols': 80})}