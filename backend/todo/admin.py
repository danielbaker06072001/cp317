from django.contrib import admin
from .models import *

# Register your models here.
class Todo_Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class User_Admin(admin.ModelAdmin):
    list_display = (
        'authToken', 
        'userId', 
        'signUp', 
        'lastLogin', 
        'firstName', 
        'lastName'
        )

class Items_Admin(admin.ModelAdmin):
    list_display = ( 
        'userId',
        'title',
        'itemId',
        'added',
        'lastAccessed'
    )

class Tag_Lookup_Admin(admin.ModelAdmin): 
    list_display = ( 
        'itemId',
        'tagId'
    )

class Tags_Admin(admin.ModelAdmin): 
    list_display = (
        'tagId',
        'tag'
    )

class Sub_Items_Admin(admin.ModelAdmin): 
    list_display = (
        'itemId',
        'characterization',
        'info'
    )

class Projects_Admin(admin.ModelAdmin): 
    list_display = ( 
        'userId',
        'title',
        'itemId',
        'added',
        'lastAccessed',
        'parentID',
        'deadline',
        'categoryTypeCode'
    )

class Project_Children_Admin(admin.ModelAdmin): 
    list_display = ( 
        'projectId',
        'childId'
    )

class Actions_Admin(admin.ModelAdmin): 
    list_display = ( 
        'userId',
        'title',
        'itemId',
        'added',
        'lastAccessed',
        'parentID',
        'deadline',
        'categoryTypeCode'
    )

class Categories_Admin(admin.ModelAdmin): 
    list_display = ( 
        "typeCode", 
        "type"
    )
    


admin.site.register(Todo, Todo_Admin)
admin.site.register(User, User_Admin)
admin.site.register(Items, Items_Admin)
admin.site.register(Tag_Lookup, Tag_Lookup_Admin)
admin.site.register(Tags, Tags_Admin)
admin.site.register(Sub_Items, Sub_Items_Admin)
admin.site.register(Projects, Projects_Admin)
admin.site.register(Project_Children, Project_Children_Admin)
admin.site.register(Actions, Actions_Admin)
admin.site.register(Categories, Categories_Admin)

