from django.db import models

# Create your models here.


from db.models import BaseModel
from tinymce.models import HTMLField
from book.enums import *

class BookManager(models.Manager):
	def get_book_by_type(self,type_id,limit=None,sort='default'):
		if sort == 'new':
			order_by = ('-create_time',)
		elif sort == 'hot':
			order_by = ('-sales',)
		elif sort == 'price':
			order_by = ('price',)
		else:
			order_by = ('-pk',)
		book_li = self.filter(type_id = type_id).order_by(*order_by)

		if limit:
			book_li = book_li[:limit]
		return book_li
	def get_books_by_id(self,books_id):
		try:
			books = self.get(id=books_id)
		except:
			books = None
		return books
class Book(BaseModel):
	book_type_chjoices = ((k,v) for k,v in BOOKS_TYPE.items())
	status_choices = ((k,v) for k,v in STATUS_CHOICE.items())

	type_id = models.SmallIntegerField(default=PYTHON,choices=book_type_chjoices)
	name = models.CharField(max_length=20,verbose_name='商品名称')
	desc = models.CharField(max_length=128,verbose_name='商品简介')
	price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='商品价格')
	unite = models.CharField(max_length=20,verbose_name='商品单位')
	stock = models.IntegerField(default=1,verbose_name='商品库存')
	sales = models.IntegerField(default=0,verbose_name='商品销量')
	detail = HTMLField(verbose_name='商品详情')
	image = models.ImageField(upload_to='books',verbose_name='商品图片')
	status = models.SmallIntegerField(default=ONLINE,choices=status_choices)

	object = BookManager()

	class Meta:
		db_table = 's_books'

