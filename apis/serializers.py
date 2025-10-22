from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #author_email = serializers.SerializerMethodField()
    author_email = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Post
        fields = ['id','post_title','post_body','author_email']

    # def get_author_email(self, obj):
    #     return obj.author.email