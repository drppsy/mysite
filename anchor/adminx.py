#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
from django.utils.html import format_html
import xadmin
from anchor.models import Anchor
from xadmin.layout import Fieldset

#
# class NotesAdmin(object):
#     list_display = ['anchor_id',"note_content"]
#     list_per_page = 20


class AnchorAdmin(object):
    list_display = ['platform','room_id','name','is_noguild','follow','room_link','note']
    list_exclude = ['value_at','redu','section_id','last_kaibo_at','update_at','is_contact','uid','id','guild_id',]
    readonly_fields = ['platform','room_id','name','is_noguild','follow','room_link',]
    search_fields = ['room_id',]
    list_filter = ['platform','is_noguild','follow',]
    form_layout = (
        Fieldset(None,
                 'platform','room_id','name','is_noguild','follow','room_link','note',
                 ),
        Fieldset(None,
                 'guild_id','value_at','redu','section_id','last_kaibo_at','update_at','is_contact','uid',**{"style":"display:None"}
                 ),
    )
    list_editable = ['note',]

    # 隐藏导出功能
    list_export = (Fieldset(None,**{"style":"display:None"}))

    list_per_page = 20


class IndexAdAdmin(object):
    list_display = ["Anchor"]

xadmin.site.register(Anchor, AnchorAdmin)
# xadmin.site.register(Notes, NotesAdmin)