from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from book.models import Book
from book.enums import *
# Create your views here.


def index(request):
	'''显示首页'''
	# 查询每个种类的3个新品信息和4个销量最好的商品信息
	python_new = Book.object.get_book_by_type(PYTHON, 3, sort='new')
	python_hot = Book.object.get_book_by_type(PYTHON, 4, sort='hot')
	javascript_new = Book.object.get_book_by_type(JAVASCRIPT, 3, sort='new')
	javascript_hot = Book.object.get_book_by_type(JAVASCRIPT, 4, sort='hot')
	algorithms_new = Book.object.get_book_by_type(ALGORITHMS, 3, sort='new')
	algorithms_hot = Book.object.get_book_by_type(ALGORITHMS, 4, sort='hot')
	machinelearning_new = Book.object.get_book_by_type(MACHINELEARNING, 3, sort='new')
	machinelearning_hot = Book.object.get_book_by_type(MACHINELEARNING, 4, sort='hot')
	operatingsystem_new = Book.object.get_book_by_type(OPERATINGSYSTEM, 3, sort='new')
	operatingsystem_hot = Book.object.get_book_by_type(OPERATINGSYSTEM, 4, sort='hot')
	database_new = Book.object.get_book_by_type(DATABASE, 3, sort='new')
	database_hot = Book.object.get_book_by_type(DATABASE, 4, sort='hot')

	# 定义模板上下文
	context = {
		'python_new': python_new,
		'python_hot': python_hot,
		'javascript_new': javascript_new,
		'javascript_hot': javascript_hot,
		'algorithms_new': algorithms_new,
		'algorithms_hot': algorithms_hot,
		'machinelearning_new': machinelearning_new,
		'machinelearning_hot': machinelearning_hot,
		'operatingsystem_new': operatingsystem_new,
		'operatingsystem_hot': operatingsystem_hot,
		'database_new': database_new,
		'database_hot': database_hot,
	}

	return render(request,'book/book_details.html',context)
def detail(request,id):
	books = Book.object.get_books_by_id(books_id = id)
	if books is None:
		return redirect(reverse('book:index'))
	books_li = Book.object.get_book_by_type(type_id=books.type_id,limit=2, sort='new')
	context = {'books':books,'books_li':books_li}
	return render(request,'book/detail.html',context)

def list(request,type_id,page):
	sort = request.GET.get('sort','default')

	if int(type_id) not in BOOKS_TYPE.keys():
		return redirect(reverse('book:index'))

	books_li = Book.object.get_book_by_type(type_id=type_id,sort=sort)

	pagintor = Paginator(books_li,1)

	num_pages = pagintor.num_pages

	if page == '' or int(page) > num_pages:
		page = 1
	else:
		page = int(page)

	books_li = pagintor.page(page)

	if num_pages < 5:
		page = range(1, num_pages + 1)
	elif page <= 3:
		page = range(1, 6)
	elif num_pages - page <= 2:
		page = range(num_pages - 4, num_pages + 1)
	else:
		page = range(page - 2, page + 3)

	# 新品推荐
	books_new = Book.object.get_book_by_type(type_id=type_id, limit=2, sort='new')

	# 定义上下文
	type_title = BOOKS_TYPE[int(type_id)]
	context = {
		'books_li': books_li,
		'books_new': books_new,
		'type_id': type_id,
		'sort': sort,
		'type_title': type_title,
		'page': page
	}


	return render(request, 'book/list.html', context)
