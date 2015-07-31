from rest_framework import exceptions
from rest_framework import serializers
from .models import MovieModel, GenreModel


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenreModel
        fields = ('genre_name', )


class MovieSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = MovieModel
        fields = ('popularity_99', 'director', 'genre', 'imdb_score', 'name')

    def to_representation(self, instance):
        ret = super(MovieSerializer, self).to_representation(instance)
        ret['99popularity'] = ret['popularity_99']
        del ret['popularity_99']
        return ret

    def to_internal_value(self, data):
        popularity_99 = data.get('99popularity')
        # validation for popularity_99
        if not popularity_99:
            raise exceptions.ValidationError({
                                '99popularity': 'This field is required.'
                                })
        else:
            if float(popularity_99) > 100.0 or float(popularity_99) < 0:
                raise exceptions.ValidationError({
                                '99popularity':
                                'This field value should be between 0 to 100.'
                                })

        director = data.get('director')
        # validation for director
        if not director:
            raise exceptions.ValidationError({
                                'director': 'This field is required.'
                                })

        genre = data.get('genre')

        imdb_score = data.get('imdb_score')
        # validation for imdb_score
        if not imdb_score:
            raise exceptions.ValidationError({
                                'imdb_score': 'This field is required.'
                                })
        else:
            if float(imdb_score) > 10.0 or float(imdb_score) < 0:
                raise exceptions.ValidationError({
                                'imdb_score':
                                'This field value should be between 0 to 10.'
                                })

        name = data.get('name')
        # validation for director
        if not name:
            raise exceptions.ValidationError({
                                'name': 'This field is required.'
                                })

        return {
                'popularity_99': float(popularity_99),
                'director': director,
                'genre': genre,
                'imdb_score': float(imdb_score),
                'name': name
              }

    def create(self, validated_data):
        new_movie = MovieModel(name=validated_data['name'],
                               director=validated_data['director'],
                               popularity_99=validated_data['popularity_99'],
                               imdb_score=validated_data['imdb_score']
                               )
        new_movie.save()
        # add genre
        for genre in validated_data['genre']:
            obj, created = GenreModel.objects.get_or_create(genre_name=genre)
            new_movie.genre.add(obj)
        return new_movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.popularity_99 = validated_data.get('popularity_99',
                                                    instance.popularity_99)
        instance.imdb_score = validated_data.get('imdb_score',
                                                 instance.imdb_score)
        instance.director = validated_data.get('director', instance.director)
        # update genre
        instance.genre = []
        for genre in validated_data['genre']:
            obj, created = GenreModel.objects.get_or_create(genre_name=genre)
            instance.genre.add(obj)
        instance.save()
        return instance
