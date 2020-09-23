from django.contrib import admin
from learning_logs.models import Topic

#register the topic model, so that the admin page can manage the model
admin.site.register(Topic)

