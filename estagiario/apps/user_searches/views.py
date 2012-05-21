# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required

@login_required
@render_to('user-searches/search-list.html')
def user_search_list(request):
    return locals()


@login_required
@render_to('user-searches/search-detail.html')
def user_search_detail(request, search_id):
    return locals()
