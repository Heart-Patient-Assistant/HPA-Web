from HPA_Apps.users.models import Feedback
from django.forms import ModelForm


class FeedBackForm(ModelForm):
    class Meta:
        model=Feedback
        fields=[
            'feedback_category',
            'rate',
            'feedback_message']
