# -*- coding: utf-8 -*-

## internships.Field
FIELD_DEFAULTS = [u'Administração', u'Direito', u'Engenharia', u'Economia', u'Informática', u'Design', u'Publicidade', u'Outros']    


## internship > company_name, company_url, company_img, company_size
COMPANIES = {
    'sparkit': {
        'name': 'SparkIT',
        'url': 'http://sparkit.com.br',
        'img': 'sparkit.png',
        'size': 'peq', },

    'vale': {
        'name': 'Vale',
        'url': 'http://vale.com.br',
        'img': 'vale.png',
        'size': 'grd', },

    'visagio': {
        'name': 'Visagio',
        'url': 'http://visagio.com',
        'img': 'visagio.png',
        'size': 'med', },
}


## address.BRAddressModel
ADDRESSES = {
    'rio': {
        'state':'rj', 'city': 'Rio de Janeiro',
        'street': 'Av Nilo Peçanha', 'number': 50,
        'district': 'Centro',
        'cep': '24444000' },

    'sg': {
        'state':'rj', 'city': 'São Gonçalo',
        'street': 'Rua Fernandes Mendonça', 'number': 72,
        'district': 'Mutuá',
        'cep': '24470060', },

    'sampa': {
        'state':'sp', 'city': 'São Paulo',
        'street': 'Av. Nações Unidas', 'number': 12551,
        'district': 'Alto de Pinheiros',
        'cep': '04578-000', }
}
