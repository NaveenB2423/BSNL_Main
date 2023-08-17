from django.urls import path
from . import views
urlpatterns = [
	path('',views.home),
	path('booksum',views.booksum),
	path('bss',views.bss),
	path('newbooking',views.newbooking,name='newbooking'),
	# path('generate',views.generate),
	path('newbooking',views.newbooking),
	path('receipt',views.receipt,name='receipt'),
	path('login',views.login),
	path('confirmletter',views.confirmletter),
	path('project',views.project,name='project'),
	path('update_data/<int:id>',views.update_data, name='update_data'),
	path('delete_data/<str:id>',views.delete_data, name='delete_data'),
]