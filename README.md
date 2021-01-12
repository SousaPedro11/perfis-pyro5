# perfis-pyro5
Projeto que implementa um RMI para cadastro de perfis implementado com Pyro5

## Preparação do ambiente
* instalar o Python
* instalar o pipenv utilizando o pip

    No Linux seria: ```sudo pip install pipenv```
* clonar o projeto
    ```shell
    git clone https://github.com/SousaPedro11/perfis-pyro5.git
    ```
* mude para o diretório raiz do projeto
### Usando Pipenv
* criar o abiente virtual
  * verificar e se preciso alterar para 3.8 a versão do Python no arquivo [Pipfile](Pipfile)
  * criar o ambiente com: ```pipenv --three```
* instalar dependências
  * entrar no shell do pipenv: ```pipenv shell```
  * instalar dependencias com: ```pipenv install```

### Usando pip
* criar o abiente virtual
  ```shell
  python -m venv venv
  ```
* Ativar o ambiente virtual
  * No Linux
    ```shell
    source ./venv/bin/activate
    ```
  * No Windows
    ```
    source .\venv\Scripts\activate
    ```
* instalar dependências
  * instalar dependencias com: ```pip install -r requirements.txt```
    
## Executar o projeto
Serão necessárias 3 instâncias de terminal
### Nameserver
Execute, no primeiro terminal, para rodar o nameserver
```shell
pyro5-ns
```
### Server
Execute, no segundo terminal, para rodar o server
```shell
python server.py
```
### Cliente
Execute, no terceiro terminal, para executar o cliente
```shell
python client.py
```
