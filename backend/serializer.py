from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'first_name', 'last_name', 'email', 'category', 'message', 'attachment', 'timestamp']