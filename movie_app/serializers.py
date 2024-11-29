from .models import Movie, Director, Review
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ("id", "name", "movie_count")

    def get_movie_count(self, director):
        return director.movies.count()
class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "director")

class ReviewSerializer(serializers.ModelSerializer):
    avarage_rating = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ("id", "text", "movie", "stars")

    def get_avarage_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum(reviews.start for review in reviews)
            avarage_rating = sum_reviews / len(reviews)
        return None


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "director", "reviews", "average_rating")