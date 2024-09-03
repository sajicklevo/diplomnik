from django_filters import rest_framework as filters
from .models import *


class FriendshipFilter(filters.FilterSet):
    status = filters.ModelChoiceFilter(queryset=FriendshipStatus.objects.all())
    profile_one = filters.ModelChoiceFilter(field_name='profile_one', queryset=Profile.objects.all())
    profile_two = filters.ModelChoiceFilter(field_name='profile_two', queryset=Profile.objects.all())

    class Meta:
        model = Friendship
        fields = ['status', 'profile_one', 'profile_two']


class ProfileFilter(filters.FilterSet):
    firstname = filters.CharFilter(field_name='firstname', lookup_expr='icontains', label='Имя')
    lastname = filters.CharFilter(field_name='lastname', lookup_expr='icontains', label='Фамилия')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains', label='Местоположение')
    gender = filters.CharFilter(field_name='gender', lookup_expr='icontains', label='Пол')
    interests = filters.ModelMultipleChoiceFilter(
        field_name='interests',
        queryset=Interest.objects.all(),
     label = 'Интересы'
    )

    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'gender', 'location', 'interests']

class GroupFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='Название')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains', label='Описание')
    group_type = filters.ChoiceFilter(field_name='group_type', choices=Group.GROUP_TYPES, label='Тип группы')
    creator = filters.CharFilter(field_name='creator', lookup_expr='icontains', label='Основатель')
    class Meta:
        model = Group
        fields = ['name', 'description', 'group_type', 'creator']