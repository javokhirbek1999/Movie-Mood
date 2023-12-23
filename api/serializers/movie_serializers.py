from rest_framework import serializers

from api.models import movie_model



class MovieSerializer(serializers.ModelSerializer):

    """Movie Serializer for Movie model."""

    class Meta:
        model = movie_model.Movie
        fields = ('id', 'title', 'description', 'slug_title', 'released_date', 'get_movie_reviews')
    

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)



class ReviewSerializer(serializers.ModelSerializer):

    """Review Serializer for Review model."""

    class Meta:
        model = movie_model.Review
        fields = ('id', 'user', 'movie', 'get_user_details', 'get_movie_details', 'content', 'rate')
        extra_kwargs = {
            'user': {'write_only': True},
            'movie': {'write_only': True}
        }