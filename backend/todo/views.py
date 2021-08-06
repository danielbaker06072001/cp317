from django.db.models.query import QuerySet
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse


"""
I ADDD THIS TO TEST
"""
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics


"""""
END
"""""

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import status

# Create your views here.

# class TodoView(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()
#     authentication_classes = []

# ========================================
# API OVERVIEW
# ========================================

@api_view(['GET'])
def apiOverview(request): 
    api_urls = { 
        'Get' : '/-list/',
        'CreateUser' : '/-create/',
        'Update' : '/-update/<str:pk>/',
        'Delete' : '/-delete/<str:pk>',
        'GetUsers': '/user/'
    } 

    return Response(api_urls)


# ========================================
# USER FUNCTIONS
# ========================================

@api_view(['GET'])
def userList(request): 
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk): 
    users = User.objects.get(authToken=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request): 
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def userUpdate(request, pk): 
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

# @api_view(['POST'])
# def userPartialUpdate(request): 
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(instance=user, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

@api_view(['DELETE', 'GET'])
def userDestroy(request, pk=None):
        user = User.objects.get(authToken=pk)
        user.delete()

        return Response("deleted")

def getUserId(auth): 
    #Gets the User's ID from the auth token 
    q1 = User.objects.filter(authToken=auth)
    return q1[0].userId


# ========================================
# Item functions
# ========================================

@api_view(['GET'])
def itemList(request, auth, lastAccessed=None):
    userId = getUserId(auth)

    #Gets filtered items by user ID
    queryset = Items.objects.filter(userId=userId)

    #if lastAccessed paramater is input, gets all items with dates that 
    #come after the lastAccessed value
    # if lastAccessed: 
    #     #translate lastAccessed into a datetime objects
    #     queryset = queryset.filter(lastAccessed=lastAccessed)

    serializer = ItemsSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request, auth, itemId): 
    userId = getUserId(auth)

    #Gets filtered items by user ID
    queryset = Items.objects.filter(userId=userId)

    #Selects item with corresponding id if possible
    try:
        item = queryset.get(itemId=itemId)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = ItemsSerializer(item, many=False)
    return Response(serializer.data)

"""
Author : Duc Minh Nguyen
-----------------------------------------------
Description : This show the todo database list
              This provide GET() and POST() method, it's gonna show what's in the databse
              If we wanna create new data use POST()
Usage : http://127.0.0.1:8000/api/todo_list/<ID_HERE>
"""
class TODO_LIST(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView) : 

    queryset= Todo.objects.all() 
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs) : 
        return self.list(request, *args, **kwargs)


    def post(self, request , *args, **kwargs ) : 
        return self.create(request, *args, **kwargs)

"""
Author : Duc Minh Nguyen
-----------------------------------------------
Description : This use to retrieve data from database using ID
              GET() method use to retrieve ID
              PUT() update the data to database
              DELETE() delete the data for good 
Usage : http://127.0.0.1:8000/api/todo_detail/<ID_HERE>
"""
class TODO_DETAIL(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView) : 
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs) : 
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs) : 
        return self.delete(request, *args, **kwargs)


"""
Author : Duc Minh Nguyen
-----------------------------------------------
Description : This use to create new item in Items database
              
Usage : http://127.0.0.1:8000/api/item/create/
"""
class ITEM_CREATE(mixins.ListModelMixin,
                    mixins.CreateModelMixin, 
                    generics.GenericAPIView): 

    queryset= Items.objects.all() 
    serializer_class = ItemsSerializer

    def get(self, request , *args, **kwargs) : 
        return self.list(request, *args, **kwargs)

    def post(self, request , *args, **kwargs) : 
        return self.create(request, *args, **kwargs)


"""
Author : Duc Minh Nguyen
-----------------------------------------------
Description : This use to create new item in Items database
              
Usage : http://127.0.0.1:8000/api/item/create/<ID_HERE>/
"""
class ITEM_UPDATE(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView) : 
    queryset= Items.objects.all() 
    serializer_class = ItemsSerializer

    def get(self, request, *args, **kwargs):            #get by searching the ID
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs) :        # Delete data in database
        return self.delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):            #update method herer
        return self.update(request, *args, **kwargs)  


"""
------------------------------------------------------------------------------------------

THE CODE FROM HERE DOWN IS INCOMPLETE
STILL NEEDS TO BE ADJUSTED AND MADE SUITABLE

"""
class ItemsViewSet(viewsets.ViewSet):
    def list(self, request, auth):
        if auth:
            q1 = User.objects.filter(authToken=auth)
        userId = q1.data.userId
        queryset = Items.objects.filter(userId=userId)
        serializer = ItemsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, auth, pk=None):
        if auth:
            q1 = User.objects.filter(authToken=auth)
        userId = q1.data.userId
        # request.data.
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)




