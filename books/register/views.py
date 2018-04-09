from django.http import JsonResponse
from django.shortcuts import render,redirect
import re
from utils.get_hash import get_hash
from django.core.urlresolvers import reverse
# Create your views here.
from register.models import Passport,Address
from utils.login_required import login_required
def register(request):

	return render(request, 'register/register.html')
def register_handler(request):
	user_name = request.POST.get('user_name')
	user_pwd = request.POST.get('pwd')
	email = request.POST.get('email')

	if not all([user_pwd,user_name,email]):
		return render(request, 'register/register.html', {'errmsg': '参数不能为空'})
	if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
		return render(request, 'register/register.html', {'errmsg': '邮箱不合法'})

	Passport.object.add_passport(user_name,user_pwd,email)
	return redirect(reverse('book/book_details.html'))
def login_check(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	remember = request.POST.get('remember')

	if not all([username,password,remember]):
		return JsonResponse({'res':2})
	passport = Passport.object.get_passport(user_name = username , user_pwd = get_hash(password))
	print(username,get_hash(password),passport)
	if passport:
		print('22222')
		next_url = request.session.get('url_path',reverse('book:index'))
		print('33333')
		jres = JsonResponse({'res':1,'next_url':next_url})

		if remember == 'true':
			print('44444')
			jres.set_cookie('username',username,max_age=7*24*3600)
		else:
			print('55555')
			jres.delete_cookie('username')
		request.session['islogin'] = True
		request.session['username'] = username
		request.session['passport_id'] = passport.id
		print('66666')
		return jres
	else:
		return JsonResponse({'res':0})
def login(request):
	return render(request,'login/login.html')

@login_required
def user(request):
	passport_id = request.session.get('passport_id')

	addr = Address.object.get_default_address(passport_id=passport_id)

	books_li = []

	context = {
		'addr':addr,
		'page':'user',
		'book_li':books_li
	}
	return  render(request,'register/user_center_info.html',context)