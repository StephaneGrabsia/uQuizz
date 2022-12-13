from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
import jwt, datetime
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/register/',
            'method': 'POST',
            'description': 'To register'
        },
        {
            'Endpoint' : '/login/',
            'method': 'POST',
            'description': 'To login'
        },      
        {
            'Endpoint' : '/user/',
            'method': 'GET',
            'description': 'get users'
        },    
        {
            'Endpoint' : '/logout/',
            'method': 'POST',
            'description': 'To logout'
        },
    ]
    return Response(routes)

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TeacherRegisterView(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        teacher_serializer = TeacherSerializer(data={'user':user.data['id']})
        teacher_serializer.is_valid(raise_exception=True)
        teacher_serializer.save()
        return Response(teacher_serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']


        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=90),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        
        response.data = {
            'jwt': token
        }
        return response

class TeacherLoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        teacher = Teacher.objects.get(user__username=username)

        if teacher is None:
            raise AuthenticationFailed('User not found')
        
        if not teacher.user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id' : teacher.user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=90),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        
        response.data = {
            'jwt': token
        }
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthentication')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthentication')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class TeacherView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthentication')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthentication')
        
        teacher = Teacher.objects.get(user__id=payload['id'])
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "success"
        }
        return response