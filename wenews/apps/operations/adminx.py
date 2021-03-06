# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/3/6 22:49'
import xadmin
from .models import UserNewsTopic, UserMessage, UserFavorite, NewsComments, UserAsk

class NewsCommentsAdmin(object):
    list_display = ['user', 'news', 'comments', 'add_time']
    search_fields = ['user', 'news', 'comments', 'add_time']
    list_filter = ['user', 'news', 'comments', 'add_time']

class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'news_name', 'add_time', ]
    search_fields = ['name', 'mobile', 'news_name' ]
    list_filter = ['name', 'mobile', 'news_name', 'add_time', ]

class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time', ]
    search_fields = ['user', 'fav_id', 'fav_type',  ]
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time', ]


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time', ]
    search_fields = ['user', 'message', 'has_read', ]
    list_filter = ['user', 'message', 'has_read', 'add_time', ]

class UserNewsAdmin(object):
    list_display = ['user', 'news', 'add_time', ]
    search_fields = ['user', 'news', ]
    list_filter = ['user', 'news', 'add_time', ]


xadmin.site.register(NewsComments, NewsCommentsAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserNewsTopic, UserNewsAdmin)