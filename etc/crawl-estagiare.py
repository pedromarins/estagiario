# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import requests

VAGAS = []
for i in range(1,16):
    res = requests.get('http://estagiare.com/page/%d/' % i)
    soup = BeautifulSoup(res.content)
    for a in soup.findAll('a', attrs={'class':'job-title'}):
        VAGAS.append(a.get('href'))
print VAGAS



</div>
>>> soup.find(attrs={'class': 'job-company-desc'}).findChildren('a')
[<a href="" target="_blank">Confidencial</a>]
>>> soup.find(attrs={'class': 'job-company-desc'}).findChildren('a')[0].text
u'Confidencial'
>>> soup.find(attrs={'class': 'job-company-desc'}).findChildren('a')[0].get('href')
u''
>>> 