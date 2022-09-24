from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register(r'Folder', FolderViewSet, basename='Folder')
router.register(r'Document', DocumentViewSet, basename='Document')
router.register(r'File', FileViewSet, basename='File')

urlpatterns = router.urls


