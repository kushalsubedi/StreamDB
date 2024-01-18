from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import (
                        OurUserRegistrationSerializer,
                           UserLoginSerializer, 
                           VerifyOTPSerializer, 
                           ResetPasswordSerializer,
                           forgetpasswordrequest
                           )
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import permissions
from .emails  import send_otp_mail
from .models import OurUser


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        # Perform user authentication here, e.g., using Django's authenticate method
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

"""
class Registerview(APIView) 
- this class is used to register a new user.
- the post method is used to create a new user.
- the post method takes request as an argument.
- the post method returns a response.
- the post method returns a response with status 201 if the user is created successfully.
- the post method returns a response with status 400 if the user is not created successfully.

### otp functionality 
- otp is generated using random module.
- otp is sent to the user's email using send_mail method.
- the user's email is retrieved from the request.data
- after otp verification user will be set to is_verified = True


"""

class Registerview(APIView):
    permission_classes = [permissions.AllowAny]  

    def post(self,request):
        try :
            serializer = OurUserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                send_otp_mail(serializer.data['email'])
                succes = {
                    "message":"User Created Successfully Check Email to verify your account",
                    "data":serializer.data,
                    "status":status.HTTP_201_CREATED
                }
                return Response({
                            
                            "data":succes,
                    })
        
            return Response({
                    "message":serializer.errors,
                    "status":status.HTTP_400_BAD_REQUEST
            })
        except Exception as e:
            return Response({
                    "message":str(e),
                    "status":status.HTTP_400_BAD_REQUEST
                }
            )

"""
class VerifyOTP(APIView): 
- this class is used to verify otp.

"""
# class VerifyOTPView(APIView):
#     permission_classes = [permissions.AllowAny] 

#     def post(self,request):
#         try :
#             data = request.data
#             serializer = VerifyOTPSerializer(data=data)
#             if serializer.is_valid(): 
#                 email = request.data.get('email')
#                 otp = request.data.get('otp')
#                 user = OurUser.objects.filter(email=email)
#                 if not user.exists():
#                     return Response({
#                         "message":"User does not exist",
#                         "status":status.HTTP_400_BAD_REQUEST
#                     })
#                 print (user.first().otp) 
#                 if not user.first().otp == otp:
#                     return Response({
#                         "message":"Invalid OTP",
#                         "status":status.HTTP_400_BAD_REQUEST
#                     })
#                 user = user.first()
#                 print ("----------------------CHECKING USER VERIFIED -----------------")
#                 print (user.is_verified)
#                 print ("----------------------CHECKING COMPLETE -----------------")
#                 user.is_verified = True
#                 print ("----------------------CHECKING USER VERIFIED AFTER FUNCTION -----------------")
#                 user.save()
#                 succes = {
#                     "message":"User Verified Successfully",
#                     "data":serializer.data,
#                     "status":status.HTTP_200_OK
#                 }
#                 return Response({
                        
#                         "data":succes,
#                     })            
#         except Exception as e:
#             return Response({
#                     "message":"validation failed",
#                     "status":status.HTTP_400_BAD_REQUEST
#                 }
#             )

class VerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = request.data
            serializer = VerifyOTPSerializer(data=data)

            if serializer.is_valid():
                email = data.get('email')
                otp = data.get('otp')

                user = get_object_or_404(OurUser, email=email)

                if not user.otp == otp:
                    return Response({
                        "message": "Invalid OTP",
                        "status": status.HTTP_400_BAD_REQUEST
                    })

                if user.is_verified:
                    return Response({
                        "message": "User is already verified",
                        "status": status.HTTP_400_BAD_REQUEST
                    })

                user.is_verified = True
                user.save()

                success = {
                    "message": "User Verified Successfully",
                    "data": serializer.data,
                    "status": status.HTTP_200_OK
                }

                return Response({
                    "data": success,
                })

        except Exception as e:
            return Response({
                "message": "Validation failed",
                "status": status.HTTP_400_BAD_REQUEST
            })

class ForgetPasswordView(APIView):
    permission_classes = [permissions.AllowAny] 

    def post (self,request):
        serializer=forgetpasswordrequest(data=request.data)
        if serializer.is_valid():
            email = serializer.get('email')
            try:
                user = OurUser.objects.get(email=email)
            except OurUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            
            if not user.is_verified:
                return Response({'error': 'User not verified'}, status=status.HTTP_401_UNAUTHORIZED)
            
            send_otp_mail(serializer.data['email'])
            return Response({
                    "message":"OTP sent to email",
                    "status":status.HTTP_200_OK
                })
           

   

        
class ResetPasswordView(APIView):
    permission_classes = [permissions.AllowAny] 

    def post(self,request):
        serializer=ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.get('email')
            try:
                user = OurUser.objects.get(email=email)
            except OurUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            if not user.is_verified:
                return Response({'error': 'User not verified'}, status=status.HTTP_401_UNAUTHORIZED)
            otp = serializer.get('otp')
        
            if not user.otp == otp:
                return Response({
                    "message":"Invalid OTP",
                    "status":status.HTTP_400_BAD_REQUEST
                })
            password = serializer.get('password')
            password2 = serializer.get('password2')
            if password != password2:
                return Response({"password": "Password fields didn't match."})
            user.set_password(password)
            user.save()
            return Response({
                    "message":"Password Reset Successful",
                    "status":status.HTTP_200_OK
                })
        return Response({
                    "message":serializer.errors,
                    "status":status.HTTP_400_BAD_REQUEST
                })

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({
                    "message":"Logout Successful",
                    "status":status.HTTP_200_OK
                })
        except :
            return Response({
                    "message":"Invalid Token",
                    "status":status.HTTP_400_BAD_REQUEST
                })
            
