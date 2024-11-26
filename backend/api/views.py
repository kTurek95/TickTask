from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from .models import Task
from .serializers import TaskSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# class CustomLoginView(APIView):
#     permission_classes = []
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # generujemy token dla użytkownika jeśli użytkownik został poprawnie uwierzytelniony
#             refresh_token = RefreshToken.for_user(user)
#             access_token = str(refresh_token.access_token) # służy do generowanie access_tokena poprzez użycie refresh tokena


#             # ustawienia ciasteczka HttpOnly na token
#             response = Response({'access_token': access_token}, status=status.HTTP_200_OK) # tworzenie odpowiedzi, która zostanie wysłana do frontendu a w niej będzie zawarty access_token
#             response.set_cookie(  # ustawienie ciasteczka HtppOnly dla refreshtokena
#                 key='refresh_token', # nazwa ciasteczka
#                 value=str(refresh_token), # wartość refresh tokena
#                 httponly=True, # ustawiamy zabieczenie HTTPONLY zeby token nie był dostępny z poziomu js, chroni to przed atakami xss
#                 secure=False, # ma być true przy używaniu https, oznacza to też że ciasteczko będzie przesyłane tylko i wyłącznie przez https
#                 samesite='None', # później ustawić na 'Lax'
#                 # max_age=7*24*60*60 # ustawiamy maksymalny czas życia ciasteczka w sekundach ( 7 dni)
#             )

#             return response
#         else:
#             # obsługa nieprawidłowego logowania
#             return Response({'detail':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class CustomRefreshView(APIView):
#     permission_classes = []

#     def post(self, request):
#         print(request.COOKIES)
#         refresh_token = request.COOKIES.get('refresh_token') # próba odczytania ciasteczka o nazwie refresh_token, które zostało utworzone w widoku CustomLoginView

#         # sprawdzamy czy token został znaleziony
#         if not refresh_token: 
#             return Response({'detail': 'Resresh token not provided'},status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             # tworzenie obiektu klasy refreshtoken z odczytanego tokena, jesli jest on poprawny to uzyskamy nowy token
#             refresh = RefreshToken(refresh_token)
#             # uzywamy refresh do wygenerowania nowego access tokena
#             new_access_token = refresh.access_token

#             # jeśli operacja się powiedziem to zwracamy nowy access token
#             return Response({'access': str(new_access_token)}, status=status.HTTP_200_OK)
#         except TokenError:
#             # jeśli nie to zostaje zwrócone error
#             return Response({'detail':'Invalid or expired refresh_token'}, status=status.HTTP_401_UNAUTHORIZED)

class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # będzie to zalogowany użytwkonik ponieważ nasza klasa jest IsAuthenticated
        
        if user.is_staff:
            return Task.objects.all()
        else:
            return Task.objects.filter(created_by=user)
        
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            print(serializer.errors)

class TaskDelete(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:
            return Task.objects.all()
        else:
            return Task.objects.filter(created_by=user)

    
    
