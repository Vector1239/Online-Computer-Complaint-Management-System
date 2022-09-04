from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_rules=[]):
	def decorator(view_func):	
		def wrapper_func(request,*args,**kwargs):
				group=None
				if request.user.groups.exists():
					group=request.user.groups.all()[0].name

				if group in allowed_rules:
					return view_func(request,*args,**kwargs)
				else:
					return HttpResponse('User is not authorized here.')
		return wrapper_func
	return decorator