from django.db import models

# Create your models here.
from db.models import BaseModel
from utils.get_hash import get_hash

class passportManger(models.Manager):
	#添加用户数据
	def add_passport(self,user_name,user_pwd,email):
		port = self.create(user_name=user_name,user_pwd=get_hash(user_pwd),email=email)
		return port

	#获取用户数据
	def get_passport(self,user_name,user_pwd):
		try:
			port = self.get(user_name=user_name,user_pwd=user_pwd)
		except:
			port = None
		return port

class Passport(BaseModel):
	user_name = models.CharField(max_length=20,verbose_name='用户名',unique=True)
	user_pwd = models.CharField(max_length=40,verbose_name='密码')
	email = models.EmailField(verbose_name='邮箱')
	is_activr = models.BooleanField(default=False,verbose_name='状态')

	object = passportManger()

	class Meta:
		db_table = 'user_login'
class AddressManager(models.Manager):
	def get_default_address(self,passport_id):
		try:
			addr = self.get(passport_id=passport_id,is_default=True)
		except:
			addr = '没有收货地址'
		return addr
	def add_one_address(self,passport_id,recipient_name,recipient_addr,zip_code, recipient_phone):
		addr = self.get_default_address(passport_id=passport_id)
		if addr:
			is_default = False
		else:
			is_default = True

		addr =  self.create(passport_id=passport_id,
							recipient_name=recipient_name,
							recipient_addr = recipient_addr,
							recipient_phone = recipient_phone,
							zip_code = zip_code,
							is_default =is_default)
		return addr

class Address(BaseModel):
	recipient_name = models.CharField(max_length=20,verbose_name='收件人')
	recipient_addr = models.CharField(max_length=256,verbose_name='收件地址')
	zip_code = models.CharField(max_length=6,verbose_name='邮政编码')
	recipient_phone = models.CharField(max_length=11,verbose_name='联系电话')
	is_default = models.BooleanField(default=False,verbose_name='是否默认')
	passport = models.ForeignKey('passport',verbose_name='账户')

	object = AddressManager()

	class Meta:
		db_table = 's_user_address'