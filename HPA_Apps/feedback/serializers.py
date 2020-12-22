from HPA_Apps.users.models import Feedback
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=("rate","feedback_category","feedback_message")


        def save(self):
            rate=self.validated_data['rate']
            feedback_category=self.validated_data['feedback_category']
            feedback_message=self.validated_data['feedback_message']
    

            feedback=Feedback.objects.create(rate,feedback_category,feedback_message)
          #  Feedback.save()
