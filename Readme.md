
# Redis Exemplo Pratico

<div align="center" style="background-color: white; padding: 10px;">
  <img src="https://portal.cin.ufpe.br/wp-content/uploads/2024/02/cropped-selo_oficial_4-2.png" alt="Logo CIN" height="120px"/>
</div>
<h2 align="center">Banco de dados Orientado à chave Valor com Redis - exemplo pratico</h2>



## 📖 Sobre o Projeto

Este projeto é um exemplo desenvolvido para o I Workshop de Engenharia de Dados do CIn-UFPE. Ele visa demonstrar a integração do Redis com aplicações Python, utilizando a biblioteca `redis-py`. Nosso Slide de Apresentação: [Banco de Dados Orientados à Chave-Valor com Redis](docs/Banco_de_Dados_orientados_à_Chave_Valor_com_Redis.pdf).

## 🚀 Tecnologias e Ferramentas

A aplicação foi desenvolvida em Python e utiliza o Redis, um armazenamento de estrutura de dados em memória conhecido por sua alta performance e flexibilidade. O Redis pode atuar como banco de dados, sistema de cache e corretor de mensagens.

## Stack do Projeto

Este projeto é uma aplicação back-end que utiliza o Redis, uma biblioteca de armazenamento de estrutura de dados em memória, para demonstrar suas capacidades e integração com Python através da biblioteca `redis-py`.

Essas e outras libs e tecnologias usadas neste projeto são:
|  Lib      | Versão    |
|-----------|-----------|
| **Runtime**           |
| Python    | v3.12.x   |
| redis     | v5.0.x    |
| **Devtime**           |
| Ruff                          | v0.4.x    |
| Docker Engine                 | vx.x.x    |
| Taskipy                       | v1.12.x   |

### Organização do projeto
```
/
├─📁 .devcontainer     ->  Configurações do devcontainer
├─📁 .vscode           ->  Definições de ambiente para o VSCode
├─📁 docs              ->  Artefatos para documentação do repo
├─📁 src               ->  [Implementação da API] 
│   ├── 📁 login
│   │      ├─🐍 login.py         ->  exemplo de login com redis e streamlit
│   │      ├─🐍 functions.py     ->  funções de uso para o login
│   │       ...
│   ├── 📁 quiz
│   │      ├─🐍 quizz.py         ->  exemplo de quiz com redis e streamlit
│   │      ├─🐍 functions.py     ->  funções de uso para do quiz
│   │       ...
│   ├── 📁 semple
│   │      ├─🐍 playground.py       -> Implementação simples é pura para demonstração
│   │   ├── 📁 functions            -> functions para o playground
│   │      ├─🐍 get.py              -> Função para obter o valor de uma chave no Redis
│   │       ...
│   │   ├── 📁 tests                -> testes para o playground
│   │       ...
│   ...
├─📄 .gitignore
├─📄 Makefile          ->  Automações para o ambiente
├─📄 pyproject.toml    ->  Definições para o projeto
├─📄 README.md
└─📄 ruff.toml         ->  Regras de linter e formatter

```

## Montando o ambiente

Este repositório esta organizando em um devcontainer.
E para instacia-lo no VSCODE é recomendado as seguintes configurações:

#### Extenções recomendadas

- Name: Remote Development
- Id: ms-vscode-remote.vscode-remote-extensionpack
- Description: An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.
- Version: 0.25.0
- Publisher: Microsoft
- VSCode Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack

#### Docker Engine

É obrigatório ter o Docker Engine já instalado e cunfigurado. Para mais informações de como instalar o Docker Engine em seu SO, ver em:

- Instruções para instalação do Docker Engine: [Ver o link](https://docs.docker.com/engine/install/)

#### Procedimento para instanciar o projeto no VSCODE
1. Com o pack de extenções instalado,
1. Realize o clone/fork deste repositório,
1. Abra o diretorio deste repositorio no VSCODE como um projeto,
1. Use o Comando _Dev Containers: Reopen in Container_ da paleta de comandos do VSCODE. _(F1, Ctrl+Shift+P)_.

Depois da compilação do container o VSCode abrirá o repositório em um ambiente encapsulado e executando diretamente de dentro do container como configurado nas definições do **/.devconainer**.

#### Procedimento para iniciar
1. inicie o ambiente virtual do poetry
```
$> poetry shell
```
2. instale as dependencias definidas no pyproject.toml
```
$> poetry install
```
- Pronto agora voce esta pronto para começar a usar!


### Principais comandos:

#### Levantar a tela de comandos do redis com python
```
$> make playground
```

#### Levantar a quizz com redis e python
```
$> make quiz
```

#### Adcionar novas dependencias
```
# Adicionar uma nova lib para o runtime do projeto
$> poetry add <<nome_da_lib>>

# Adicionar uma nova lib para o ambiente de desenvolvimento
$> poetry add <<nome_da_lib>> --group dev
```

#### Se preferir utilizar Um gerenciador de desktop Redis [cliente GUI] Simples:

```
# Instalação Linux:
$> sudo snap install another-redis-desktop-manager
```
# para mais informações:
consulte o Github [Link](https://github.com/qishibo/AnotherRedisDesktopManager).
