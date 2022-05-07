from rest_framework import serializers
from tasklist import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "timestamp",
            "description",
            "completed",
            "updated",
            "user",
        )
        model = models.Task
