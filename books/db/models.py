from django.db import models

class BaseModel(models.Model):
	is_delect = models.BooleanField(default=False,verbose_name='是否删除')
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now=TabError,verbose_name='修改时间')

	class Meta:
		abstract = True