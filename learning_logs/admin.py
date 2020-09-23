from django.contrib import admin
from learning_logs.models import Topic,Entry

#register the topic model, so that the admin page can manage the model
admin.site.register( Topic )
admin.site.register( Entry )
