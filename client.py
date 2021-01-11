import Pyro5.api

pessoa = {
    'email': 'email@gmail.com',
    'nome': 'Joao',
    'sobrenome': 'Almeida',
    'residencia': 'Belém',
    'foto': ''
}

formacao = {
    'nome': 'Sistemas de Informacao',
}

habilidade = {
    'nome': 'Ciencia  de Dados',
}

habilidade1 = {
    'nome': 'Web Developer',
}

experiencia = {
    'nome': 'Estagio em Desenvolvimento de Software',
}

experiencia1 = {
    'nome': 'Desenvolvedor Python',
}

perfil_maker = Pyro5.api.Proxy('PYRONAME:perfis')
perfil_maker.open_session()
print(perfil_maker.cadastrar_perfil(experiencia, formacao, habilidade, pessoa))
print(perfil_maker.cadastrar_perfil(experiencia, formacao, habilidade1, pessoa))
print(perfil_maker.cadastrar_perfil(experiencia1, formacao, habilidade, pessoa))
print(perfil_maker.listar_pessoas())
perfil_maker.close_session()
