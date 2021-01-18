from django import forms
# ================ user learns models import ===programming questions models import =======
from .models import (
                    # ================ user learns models import
                    Subject,
                    Topic,
                    Learn,
)

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']


class LearnForm(forms.ModelForm):
    class Meta:
        model =Learn
        fields =['lession_type','lession']