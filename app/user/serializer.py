from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from .models import UserModel
from . import mensagens


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "uuid",
            "username",
            "password",
        )

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)

        mandatory_fields = {
            "username": mensagens.MSG2.format(u"Usuario"),
            "password": mensagens.MSG2.format(u"Senha"),
        }

        for key, value in mandatory_fields.items():
            self.fields[key].error_messages["required"] = value
            self.fields[key].error_messages["blank"] = value
            self.fields[key].error_messages["null"] = value



    def validate(self, data):
        
        if data.get('password') == data.get('username'):
            raise serializers.ValidationError(
                "Isso daí ta errado, hein? Procura uma senha diferente, fião!"
            )