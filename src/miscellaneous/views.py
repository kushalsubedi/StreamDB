
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import FAQserializer , FAQ_Details_serializer, TermsAndConditionsSerializer, PrivacyPolicySerializer
from .models import FAQ, TermsAndConditions, PrivacyPolicy

@api_view(['GET'])
@permission_classes([AllowAny])
def FAQ_list(request):
    if request.method == 'GET':
        faq = FAQserializer()
        return Response(faq.data, status=status.HTTP_200_OK)
    return Response(faq.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def FAQ_Details (request,pk):
    try:
        faq = FAQ_Details_serializer .objects.get(pk=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FAQ_Details_serializer(faq)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TermsAndConditionsAPIView(generics.ListAPIView):
    queryset = TermsAndConditions.objects.all()
    serializer_class = TermsAndConditionsSerializer

class PrivacyPolicyAPIView(generics.ListAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer