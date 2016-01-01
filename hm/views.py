from django.shortcuts import render
from hm import templatenames
from hm.forms import LoginForm, RegisterForm, SelectServiceForm
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from hm import methods
from haversine import haversine
from decimal import Decimal
from hm.models import Mechanic
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models.UserManager import create_user 
from django.contrib.auth.models import User


class IndexView(TemplateView):
	template_name = templatenames.INDEX	
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context = { 'user': self.request.user	}
		return context
class LoginView(FormView):
	form_class = LoginForm
	template_name = templatenames.LOGIN
	def get_context_data(self, **kwargs):
		context = super(LoginView,self).get_context_data(**kwargs)
		return context
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	auth_login(self.request, form.get_user())
        	if self.request.session.test_cookie_worked():
           		self.request.session.delete_test_cookie()
        	return HttpResponseRedirect(redirect_to)
		
	def form_invalid(self,form):
		return super(LoginView,self).form_invalid(form)
class RegisterView(FormView):
	form_class = RegisterForm
	template_name = templatenames.REGISTER
	def get_context_data(self, **kwargs):
		context = super(RegisterView,self).get_context_data(**kwargs)
		return context
	def form_valid(self,form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		password_again = form.cleaned_data['password_again']
		usernames = methods.retrieve_all_usernames()
		if password == password_again and username not in usernames:
			create_user(username, password)
		
		return super(RegisterView, self).form_valid(form)
	def form_invalid(self,form):

		return super(RegisterView, self).form_invalid(form)	

class SelectServiceView(FormView):
	
	form_class = SelectServiceForm
	template_name = templatenames.SELECT_SERVICE
	def get_context_data(self, **kwargs):
		context = super(SelectServiceView,self).get_context_data(**kwargs)
		context ={ 'user_lati':self.request.session.get('user_latitude'), 'user_long':self.request.session.get('user_longitude')}
 
		return context
	def form_valid(self,form):
		return super(SelectServiceView, self).form_valid(form)
	def form_invalid(self,form):
		return super(SelectServiceView, self).form_invalid(form)

class ConfirmLocationView(RedirectView):
	permanent=True
	url = templatenames.service_select
	template_name = templatenames.CONFIRM_LOCATION
	pattern_name = templatenames.pattern_select_service
	def get_redirect_url(self, *args, **kwargs):
		context = super(ConfirmLocationView,self).get_redirect_url(*args,**kwargs)
		if self.request.method == 'GET':	
			self.request.session['user_longitude'] = self.request.GET.get('long')
			self.request.session['user_latitude'] = self.request.GET.get('lati')
			
		return context	

class SearchMechanicsView(RedirectView):
	permanent=True
	url = templatenames.user_waiting
	pattern_name = templatenames.search_mechanics
	def get_redirect_url(self, *args, **kwargs):
		context = super(SearchMechanicsView,self).get_redirect_url(*args,**kwargs)
		user_latitude = str(self.request.session['user_longitude'])
		user_longitude =str(self.request.session['user_latitude'])
		user_location = (float(user_latitude),float(user_longitude))
		mechanics = Mechanic.objects.all()	
		MECHANIC_QUERY_LIST = list()
		for mechanic in mechanics:		
			mechanic_latitude = mechanic.latitude 
			mechanic_longitude = mechanic.longitude
			
			mechanic_location = (mechanic_latitude, mechanic_longitude)
			distance = haversine( user_location, mechanic_location )
			if distance < templatenames.MAX_THRESHOLD_INITIAL :
				mechanic_object = dict()
				mechanic_object['distance'] = distance 
				mechanic_object['mechanic'] = mechanic
				MECHANIC_QUERY_LIST.append(mechanic_object)
		self.request.session['mechanic_query_list'] = MECHANIC_QUERY_LIST
					
		return context	

class MechanicReceiveRequestView(TemplateView):
	template_name = templatenames.MECHANIC_SERVICE_REQUEST
	def  get_context_data(self, **kwargs):
		context = super(MechanicServiceRequestView,self).get_context_data(**kwargs)
		return context

class UserServiceRequestView(TemplateView):
	template_name = templatenames.USER_SERVICE_REQUEST
	def  get_context_data(self, **kwargs):
		context = super(UserServiceRequestView,self).get_context_data(**kwargs)
		return context
	
class ChatBoxView(TemplateView):
	template_name = templatenames.CHAT_BOX
	def get_context_data(self, **kwargs):
		context = super(ChatBoxView,self).get_context_data(**kwargs)
		return context

class PaymentGatewayView(FormView):
	
	template_name = templatenames.PAYMENT_GATEWAY
	def get_context_data(self, **kwargs):
		context = super(PaymentGateway,self).get_context_data(**kwargs)
		return context
	def form_valid(self,form):
		return super(PaymentGatewayView, self).form_valid(form)
	def form_invalid(self,form):
		return super(PaymentGatewayView, self).form_invalid(form)

class UserWaitingView(TemplateView):
	template_name = templatenames.USER_WAITING
	def get_context_data(self, **kwargs):
		context = super(UserWaitingView, self).get_context_data(**kwargs)
		context = { 'mechanics':self.request.session.get('mechanic_query_list'), 'ulat':self.request.session.get('user_latitude'), 'ulong':self.request.session.get('user_longitude'),}	
			
		
		return context
