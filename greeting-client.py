import Pyro5.api

name = input('Qual seu nome? ').strip()
greeting_maker = Pyro5.api.Proxy('PYRONAME:example.greeting')
print(greeting_maker.get_fortune(name))
