from django.conf.urls import url
from hm.views import IndexView, LoginView, RegisterView,  ConfirmLocationView, MechanicReceiveRequestView, UserServiceRequestView, ChatBoxView, PaymentGatewayView, SelectServiceView, SearchMechanicsView, UserWaitingView

urlpatterns=[
	url(r'^$', 			IndexView.as_view(), 			name='index'),
	url(r'^accounts/login/$', 	LoginView.as_view(), 			name='login'),
	url(r'^accounts/register/$', 	RegisterView.as_view(), 		name='register'),
	url(r'^service/select/', 	SelectServiceView.as_view(), 		name='selectservice'),
	url(r'^location/confirm', 	ConfirmLocationView.as_view(), 		name='confirmlocation'  ),
	url(r'^request/service/', 	UserServiceRequestView.as_view(), 	name='userservicerequest' ),
	url(r'^search/mechanics/', 	SearchMechanicsView.as_view(),		name='searchmechanics'),
	url(r'^user/wait/',		UserWaitingView.as_view(),		name='userwaiting'),
	url(r'^receive/request/', 	MechanicReceiveRequestView.as_view(), 	name='mechanicreceiverequest' ),
	url(r'^chat/', 			ChatBoxView.as_view(), 			name='chatbox'  ),
	url(r'^secure/payment', 	PaymentGatewayView.as_view(), 		name='paymentgateway'),
] 


