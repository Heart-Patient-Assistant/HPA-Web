from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import CreateAccountSerializer,EditingProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework import permissions,serializers



from HPA_Apps.users.models import Profile

#creating new account and send back the token 
@api_view(['POST','GET'])
@permission_classes([permissions.AllowAny])
def createaccount(request):
    serializer=CreateAccountSerializer(data=request.data)
    
    data={}

    if request.method=='POST':
        if serializer.is_valid():
            account,acountType=serializer.save()    #serializer's save function return bothbaccount object, string representation of account type
            
            data['created']='account successfully created'
            data['email']=account.email
            
            data['type']=acountType

            token=Token.objects.get(user=account).key
            data['token']=token
        
        else:
            data=serializer.errors  #returning erros in serializer class
    else:
            data={
                "required fields":['email','first_name','last_name','password','password2'," type: DOCTOR or PATIENT"]
            }
    return Response(data)

#updating profile 

@api_view(['POST','GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def editprofile(request):
    data={}
    token=request.auth
    serializer=EditingProfileSerializer(data=request.data)

    if request.method=='POST':
        if serializer.is_valid():
            
            serializer.save(token)
            data['updated']='profile successfully updated'

        else:
    
            raise serializers.ValidationError({"error in data":"please chech data input formate to be 'y-m-d' "})
    else:
        data['Location']="input your location"
        data['birth_date']="input your birth data y-m-d "
    
    return Response(data)
