#-*- coding:utf-8 -*-

from django.db import models
from datetime import datetime


class News(models.Model):
	STATUS_CHOICES = (
		('0', '显示在新闻列表中'),
		('1', '不显示在新闻列表中'),
	)

	title = models.CharField('新闻标题', max_length=30)
	content = models.TextField('新闻内容')
	ctime = models.DateTimeField('创建时间', max_length=30, default=datetime.now())
	utime = models.DateTimeField('最新修改时间', max_length=30, default=datetime.now())
	status = models.CharField('状态', max_length=3, default='0', choices=STATUS_CHOICES)

	class Meta:
		verbose_name = '新闻'
		verbose_name_plural = '新闻'

	def __unicode__(self):
		return self.title
