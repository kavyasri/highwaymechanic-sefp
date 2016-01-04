from django.conf.urls import url
from hm.views import IndexView, LoginView, RegisterView,  ConfirmLocationView, MechanicReceiveRequestView, UserServiceRequestView, ChatBoxView, SelectServiceView, SearchMechanicsView, UserWaitingView
from django.contrib.auth.decorators import login_required

urlpatterns=[
	url(r'^$', 			login_required(IndexView.as_view()), 			name='index'),
	url(r'^accounts/login/$', 	LoginView.as_view(), 					name='login'),
	url(r'^accounts/register/$', 	RegisterView.as_view(), 				name='register'),
	url(r'^service/select/', 	login_required(SelectServiceView.as_view()), 		name='selectservice'),
	url(r'^location/confirm', 	login_required(ConfirmLocationView.as_view()), 		name='confirmlocation'  ),
	url(r'^request/service/', 	login_required(UserServiceRequestView.as_view()), 	name='userservicerequest' ),
	url(r'^search/mechanics/', 	login_required(SearchMechanicsView.as_view()),		name='searchmechanics'),
	url(r'^user/wait/',		login_required(UserWaitingView.as_view()),		name='userwaiting'),
	url(r'^receive/request/', 	login_required(MechanicReceiveRequestView.as_view()), 	name='mechanicreceiverequest' ),
	url(r'^chat/', 			login_required(ChatBoxView.as_view()), 			name='chatbox'  ),
] 


