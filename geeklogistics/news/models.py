#-*- coding:utf-8 -*-

from django.db import models
from datetime import datetime


class News(models.Model):
	title = models.CharField('新闻标题', max_length=30)
	content = models.TextField('新闻内容')
	ctime = models.DateTimeField('创建时间', max_length=30, default=datetime.now())
	utime = models.DateTimeField('最新修改时间', max_length=30, default=datetime.now())
	status = models.CharField('状态', max_length=3, default=0)

	class Meta:
		verbose_name = '新闻'
		verbose_name_plural = '新闻'

	def __unicode__(self):
		return self.title
