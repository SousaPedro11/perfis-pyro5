import Pyro5.api

pessoa = {
    'email': 'email@gmail.com',
    'nome': 'Joao',
    'sobrenome': 'Almeida',
    'residencia': 'Belém',
    'foto': ''
}

pessoa1 = {
    'email': 'email1@gmail.com',
    'nome': 'Edmilton',
    'sobrenome': 'Peixeira',
    'residencia': 'Belém',
    'foto': ''
}

pessoa2 = {
    'email': 'jose@gmail.com',
    'nome': 'José',
    'sobrenome': 'Jesus',
    'residencia': 'Marituba',
    'foto': ''
}

formacao = {
    'nome': 'Sistemas de Informacao',
}

formacao1 = {
    'nome': 'Ciencias da Computacao',
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
perfil_maker.cadastrar_perfil(experiencia, formacao, habilidade, pessoa)
perfil_maker.cadastrar_perfil(experiencia, formacao, habilidade, pessoa1)
perfil_maker.cadastrar_perfil(experiencia, formacao, habilidade1, pessoa1)
perfil_maker.cadastrar_perfil(experiencia, formacao, habilidade1, pessoa)
perfil_maker.cadastrar_perfil(experiencia1, formacao, habilidade, pessoa)
perfil_maker.cadastrar_perfil(experiencia1, formacao1, habilidade1, pessoa2)
print('Q1')
print(perfil_maker.pessoas_por_formacao(formacao))
print('Q2')
print(perfil_maker.pessoas_por_cidade('Belém'))
print('Q3')
print(perfil_maker.adicionar_experiencia(pessoa2, experiencia))
print('Q4')
print(perfil_maker.experiencia_por_perfil('jose@gmail.com'))
print('Q5')
print(perfil_maker.listar_pessoas())
print('Q6')
print(perfil_maker.get_perfil_by_id('email1@gmail.com'))
perfil_maker.close_session()
