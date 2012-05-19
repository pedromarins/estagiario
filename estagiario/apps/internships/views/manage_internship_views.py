# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404
from annoying.decorators import render_to
from internships.forms import InternshipForm
from internships.models import Internship



@render_to('internships/manage/add-internship.html')
def add_internship(request):
    "Publishes a new internship opening"
    form = InternshipForm(request.POST or None)
    if form.is_valid():
        internship = form.save()
        return redirect('edit_internship', internship_id=internship.id)

    return locals()

@render_to('internships/manage/edit-internship.html')
def edit_internship(request, internship_id):
    internship = get_object_or_404(Internship, pk=internship_id)
    return locals()


