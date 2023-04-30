from django.urls import path
import core.views
from rest_framework.routers import DefaultRouter


urlpatterns = [

]

router = DefaultRouter()
router.register('addresses', core.views.AddressViewSet)
router.register('universities', core.views.UniversityViewSet)
router.register('departments', core.views.DepartmentViewSet)
router.register('professors', core.views.ProfessorViewSet)

urlpatterns += router.urls
