from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer


class CreateTodoAPIView(generics.CreateAPIView):
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("serializer", serializer)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        print("serializer.data==>", serializer.data)
        headers = self.get_success_headers(serializer.data)
        print("headers==>", headers)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get(self, request):
        return Response('Hello world')