from django.contrib admin
from django.urls import path
url patterns=[
	path('admin/',admin.site urls),
	path('f/',views.first,name="first"),
	]