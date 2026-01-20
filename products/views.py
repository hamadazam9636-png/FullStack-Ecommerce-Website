from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing products
    - list: GET all products (public)
    - create: POST new product (admin only)
    - retrieve: GET specific product (public)
    - update: PUT/PATCH product (admin only)
    - destroy: DELETE product (admin only)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        """
        Different permissions based on action
        - list, retrieve: public
        - create, update, destroy: admin only
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """Automatically set the created_by user"""
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        """Keep the original creator"""
        serializer.save()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, IsAdminUser])
    def owner_products(self, request):
        """Get all products created by the current owner/admin"""
        products = Product.objects.filter(created_by=request.user)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def available_products(self, request):
        """Get only available products"""
        products = Product.objects.filter(available=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
class CustomAuthToken(ObtainAuthToken):
    """
    Custom login view that returns token for React admin login.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'is_staff': user.is_staff
        })
