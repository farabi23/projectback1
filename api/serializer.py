from rest_framework import serializers

from api.models import Company, Vacancy, People, Products


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('description'),
                                         address=validated_data.get('address'))

        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.address = validated_data.get('address')
        instance.save()
        return instance


# serializerModelserialzier
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ("id", 'name', 'description', 'salary',)


class PeopleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()

    def create(self, validated_data):
        people = People.objects.create(name=validated_data.get('name'),
                                       age=validated_data.get('age'))
        return people

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.age = validated_data.get('age')
        instance.save()
        return instance


# serializerModelserializer
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price')
