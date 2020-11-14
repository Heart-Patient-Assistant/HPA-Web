from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import CreateAccountSerializer
from rest_framework.authtoken.models import Token
from rest_framework import permissions


@api_view(['POST','GET'])
@permission_classes([permissions.AllowAny])
def createaccount(request):
    serializer=CreateAccountSerializer(data=request.data)
    
    data={}
    
    if serializer.is_valid():
        account=serializer.save()
        
        data['created']='account successfully created'
        data['email']=account.email

        token=Token.objects.get(user=account).key
        data['token']=token
    
    else:
        data=serializer.errors  #returning erros in serializer class
    
    return Response(data)