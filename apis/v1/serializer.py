from rest_framework.serializers import ModelSerializer
from app.models import book

class bookSerializers(ModelSerializer):
    class Meta:
        model=book
        fields="__all__"
