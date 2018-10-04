from django.urls import path
from . import views
urlpatterns=[
	path('', views.index),
	path('delete/<int:course_id>',views.delete),
	path('add', views.add),
	path('warning', views.warning),
	path('begone/<int:course_id>', views.begone)
]