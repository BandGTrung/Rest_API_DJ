from rest_framework import serializers
from .models import Pets,Cat,Dog,Fish

class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = "__all__"

class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = "__all__"

class FishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fish
        fields = "__all__"

class PetSerializer(serializers.ModelSerializer):
    cats = CatSerializer(many=True)
    dogs = DogSerializer(many=True)
    fishes = FishSerializer(many=True)
    class Meta:
        model = Pets
        fields = ['id','type','cats','dogs','fishes']