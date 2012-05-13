# -*- coding: utf-8 -*-

COMPANIES = {
    'sparkit': {
        'name': 'SparkIT',
        'url': 'http://sparkit.com.br',
        'img': 'sparkit.png',
        'size': 'peq',
    },

    'vale': {
        'name': 'Vale',
        'url': 'http://vale.com.br',
        'img': 'vale.png',
        'size': 'grd',
    },

    'visagio': {
        'name': 'Visagio',
        'url': 'http://visagio.com',
        'img': 'visagio.png',
        'size': 'med',
    },
}


ADDRESSES = {
    
    'rio': {
        'state':'rj', 'city': 'Rio de Janeiro',
        'street': 'Av Nilo Peçanha', 'number': 50
        'district': 'Centro',
        'cep': '24444000' }

    'sg': {
        'state':'rj', 'city': 'São Gonçalo',
        'street': 'Rua Fernandes Mendonça', 'number': 72
        'district': 'Mutuá',
        'cep': '24470060', }

    'sampa': {
        'state':'sp', 'city': 'São Paulo',
        'street': 'Rua Fernandes Mendonça', 'number': 72
        'district': 'Mutuá',
        'cep': '24470060', }

}



def fill_company(ins, company, **kwargs):
    data = COMPANIES[company]
    for k,v in kwargs:
        data[k] = v
    ins.company_name    = data['name']
    ins.company_url     = data['url']
    ins.company_img     = 'company_logos/' + data['img']
    ins.company_size    = data['size']
    return ins

def fill_address(ins, addr):
    data = ADDRESSES[addr]
    state = State.objects.get(uf=data['state'])[0]
    city = City.objects.filter(state=state).filter(name__iexact=data['city'])

    ins.street = data['street']
    ins.number = data['number']
    #ins.complement = data['complement']
    ins.district = data['district']
    ins.cep = data['cep']
    
    ins.city = city
    ins.state = state
    return ins






    
