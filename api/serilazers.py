from rest_framework import serializers
from place.models import Place,Comment,User


class PlaceSerilazers(serializers.Serializer):

    name=serializers.CharField()
    description=serializers.CharField()
    addres=serializers.CharField()
    place_img=serializers.ImageField()

    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        addres = validated_data.get('addres')
        place_img = validated_data.get('place_img')

        place_instance = Place.objects.create(
            name=name,
            description=description,
            addres=addres,
            place_img=place_img
        )
        return place_instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'
    
        