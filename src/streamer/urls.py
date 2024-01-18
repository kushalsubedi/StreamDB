
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework.schemas import get_schema_view
#from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




LOCAL_APPS = [
    'authentication',
    'miscellaneous',
    'content',
]

   
urlpatterns = [
    path('admin/', admin.site.urls),  
]


## Apps that were installed by using PIP
Third_Party_Apps = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

## Apps that were created locally
local_Apps = [
    path('api/', include('authentication.urls'), name='authentication'),
    path('misc/', include('miscellaneous.urls'), name='miscellaneous'),
    path('content/', include('content.urls'), name='content'),
]

'''urlpatterns += [
    # ...
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    # ...
]
'''

urlpatterns += local_Apps+Third_Party_Apps
