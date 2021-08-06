from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Todo
        fields = ('id', 'title', 'description', 'completed')

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('signUp', 'lastLogin', 'firstName', 'lastName')

class ItemsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Items
        fields = ('userId','title', 'itemId', 'added', 'lastAccessed')  # I added the userId because it's require

class Tag_lookupSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Tag_Lookup
        fields = ('tagId', 'tag') 

class TagsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tags
        fields = ('tagId', 'tag')

class Sub_ItemsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Sub_Items
        fields = ('itemId', 'characterization', 'info')

class ProjectsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Projects
        fields = (
            'title', 
            'itemId', 
            'added', 
            'lastAccessed', 
            'parentID',
            'deadline', 
            'categoryTypeCode'
        )

class Project_ChildrenSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Project_Children
        fields = ('projectId', 'childId')

class ActionsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Actions
        fields = (
            'title', 
            'itemId', 
            'added', 
            'lastAccessed', 
            'parentID',
            'deadline', 
            'categoryTypeCode'
        )


class CategoriesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Categories
        fields = ( 
            'typeCode',
            'type'
        )