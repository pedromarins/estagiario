# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from annoying.decorators import render_to
from forms import InternshipForm


@render_to('add_internship.html')
def add_internship(request):
    form = InternshipForm(request.POST or None)
    if form.is_valid():
        ins = form.save()
        return redirect(ins)
        
    return locals()
