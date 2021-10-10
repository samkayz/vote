from django.urls import path, include
from vote.views import *

urlpatterns = [
    path('vote/', include('vote.urls')),
    path('', IndexPage.as_view(), name='index'),
    path('getpollingunit/', GetPollingUnit.as_view(), name='getpollingunit'),
    path('pu_result/', GetPUResult.as_view(), name='pu_result'),
    path('resultsbylga/', GetResultByLGA.as_view(), name="resultsbylga"),
    path('addresult/', AddResult.as_view(), name='addresult'),
]
