from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
# Create your views here.
    

# In sessionAuthentication we need to provide the url separately in the path in order to login into apiview for crud
class StudentCRUD(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAdminUser]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    #permission_classes = [DjangoModelPermissions] # this field give to power to add each things separately in the 
    # admin panel like given only update or delete or view option or delete any permission or authorization as 
    #per your need this is what DjangoModelPermssions gives you the control over it 

    # Authenticated but only has permission to read only, except all other functionalities provided that user must be login in order to see or manuplate
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # same as DjangoModelPermission but it has already only view the api detail
    # whereas DjangoModelPermission Do not have read permission too 
    # and it can also add like munu which has previously DjangoModelPermission set the all update,del,view , permission
    #which means we can login into it with previous admin


