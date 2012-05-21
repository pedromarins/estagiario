# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from annoying.decorators import render_to
from envelope.views import ContactView

@render_to('index.html')
def index(request):
    #print request.user.is_authenticated()
    #return locals()
    return redirect('/estagios/')

ENVELOPE_VIEW = {
    'template_name': "envelope/contato.html", #'success_url':"/",    
}

contato = ContactView.as_view(**ENVELOPE_VIEW)