from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, UserDetailSerializer
from .models import Todo

User = get_user_model()


@api_view(['POST']) # 특정 메소드의 요청만 처리
def todo_create(request):
    # request.data 는 axios 의 body 로 전달한 데이터
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # 사용자가 새롭게 작성한 데이터를 응답해준다. 
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(reaquest, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    # 수정하거나 삭제할 todo instance 호출 
    if reaquest.method == 'PUT':
        # instance todo 를 request.data 로 넘어온 값으로 수정하겠다. 
        serializer = TodoSerializer(instance=todo, data=reaquest.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if reaquest.method == 'DELETE':
        todo.delete()
        # 204 == '삭제했습니다' status code 
        return Response(status=204) # 요청에 성공했지만 컨텐츠는 없다는걸 알려주는 status code


@api_view(['GET'])
def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserDetailSerializer(instance=user)
    return Response(serializer.data)
