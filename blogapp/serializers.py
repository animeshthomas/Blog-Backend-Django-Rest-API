from rest_framework import serializers
from blogapp.models import blogAdd

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=blogAdd
        fields=(
            'userid',
            'title',
            'message'
        )