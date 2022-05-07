# from rest_framework import generics
# from tasklist import models
# from .serializers import TaskSerializer
#
#
# class TasklistView(generics.ListCreateAPIView):
#     queryset = models.Task.objects.all()
#     serializer_class = TaskSerializer
#
#


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from tasklist.models import Task
from .serializers import TaskSerializer

class TasklistView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        tasks = Task.objects.filter(user = request.user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'title': request.data.get('title'),
            'timestamp': request.data.get('timestamp'),
            'description': request.data.get('description'),
            'completed': request.data.get('completed'),
            'updated': request.data.get('updated'),
            'user': request.user.id
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer