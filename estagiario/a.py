class A(object):
    class B:
        b = 'bbb'
    class A:
        aa = 'aaa'
    class Meta:
        mm = 'META'
    def __init__(self):
        print self.B.b
        print self.A.aa
        print getattr(self.Meta, 'mm', 'Maaaa')
        print getattr(self.B, 'mm', 'Baaaa')
        # print self.Meta.get('amm', 'Mamm')
        # print self.B.get('amm', 'BBBBBM')

A()        