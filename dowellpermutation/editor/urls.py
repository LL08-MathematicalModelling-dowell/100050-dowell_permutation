from django.template.defaulttags import url
from editor.views import *

urlpatterns = [
    url('', IndexView.as_view(), name="IndexView"),
]
