from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
import rest_framework
from rest_framework import serializers


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

from rest_framework.views import APIView
from rest_framework import status

from rest_framework import mixins, generics, viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet




def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )
#*Function based view
# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello World!"})

# @api_view(['GET'])
# def todoList(request):
#     queryset = Todo.objects.all()
#     serializer = TodoSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def todoCreate(request):
#     serializer = TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['GET','POST'])
# def todoListCreate(request):
#     if request.method == 'GET':
#         queryset = Todo.objects.all()
#         serializer = TodoSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def todoUpdate(request, pk):
#     queryset=Todo.objects.get(id=pk)
#     if request.method == 'GET':
#         serializer = TodoSerializer(queryset)
#         return Response(serializer.data)
        
#     elif request.method == 'PUT':
#         serializer = TodoSerializer(instance=queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response("Item deleted successfully", status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['DELETE'])
# def todoDelete(request, pk):
#     queryset=Todo.objects.get(id=pk)
#     queryset.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# class TodoList(APIView):
#     def get(self, request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TodoDetail(APIView):

#     def get_obj(self, id):
#         todo = get_object_or_404(Todo, pk=id)

#     def get(self, request, id):
#         todo = self.get_obj(id)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         todo = self.get_obj(id)
#         serializer = TodoSerializer(instance=todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         todo = self.get_obj(id)
#         todo.delete()
#         data = {
#             "message": "Todo with id `{}` has been deleted successfully.".format(id)
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)


# class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class TodoListCreate(ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer



# class TodoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     lookup_field = 'id'

class TodoMVS(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer