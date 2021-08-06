from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model): 
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class User(models.Model): 
    authToken = models.CharField(max_length=120)
    userId = models.AutoField(primary_key=True)
    signUp = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(default=datetime.now)
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)

    def __str__(self) -> str:
        return (self.firstName + " " + self.lastName)

class Items(models.Model): 
    userId = models.IntegerField()  
    title = models.CharField(max_length=120)
    itemId = models.AutoField(primary_key=True)
    added = models.DateTimeField(default=datetime.now)
    lastAccessed = models.DateTimeField(default=datetime.now)

class Tag_Lookup(models.Model): 
    itemId = models.IntegerField()
    tagId = models.AutoField(primary_key=True)

class Tags(models.Model):
    tagId = models.IntegerField()
    tag = models.CharField(max_length=120)

class Sub_Items(models.Model): 
    itemId = models.IntegerField()
    characterization = models.CharField(max_length=120)
    info = models.TextField()

class Projects(Items): 
    parentID = models.IntegerField()
    deadline = models.DateTimeField(default=datetime.now)
    categoryTypeCode = models.CharField(max_length=10)

class Project_Children(models.Model): 
    projectId = models.IntegerField()
    childId = models.IntegerField()

class Actions(Items): 
    parentID = models.IntegerField()
    deadline = models.DateTimeField(default=datetime.now)
    categoryTypeCode = models.CharField(max_length=10)

class Categories(Items):
    typeCode = models.CharField(primary_key=True, max_length=120)
    type = models.CharField(max_length=120, default="typeless")