from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.models import Comment, Post, Group, Follow
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()


class GroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class FollowSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
            ),
        )

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError
        return value
