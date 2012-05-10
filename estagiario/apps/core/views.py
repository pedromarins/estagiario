# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from envelope.views import ContactView

@render_to('index.html')
def index(request):
    return locals()

ENVELOPE_VIEW = {
    'template_name': "envelope/contato.html", #'success_url':"/",    
}

contato = ContactView.as_view(**ENVELOPE_VIEW)