# ICard

## Quadro de Tarefas
Clique [aqui](https://github.com/Maharal/ICard/projects/1) para acessar nosso quadro de tarefas

**Alunos:**
- Guilherme Miranda
- Raphael Augusto Teixeira Silva
- Wanderson Sena
- Victor Hugo Silva Moura

**Descrição:** 
O objetivo do ICard é ser uma plataforma web de cartões de visita digital. A grande vantagem do nosso sistema para os usuários é que eles possuem uma alta flexibilidade de como compartilhar seus cartões de visita, pesquisar por cartões de outros usuários, e tira a necessidade de gastar dinheiro com impressão.

**Escopo funcional:**
- O usuário pode criar um cadastro
- O usuário pode pesquisar por outros usuários cadastrados
- O usuário pode pesquisar por cartões
- O usuário pode criar N cartões
- O usuário pode editar os cartões
- O usuário pode salvar alguns cartões como favoritos

**Escopo tecnológico:**
- *backend:* python, Django, PostgreSQL e Heroku
- *frontend:* javascript, css e html

Deploy no Heroku:

- Instalar o Heroku CLI
 ```
heroku git:remote -a -i-card
git push -u heroku main
```

Url: https://i-card.herokuapp.com/

## Sprint 1

### Histórias e tarefas
- Ter uma aplicação de DJango e conseguir subir para o heroku (Raphael e Wanderson)
- Ter o site rodando no heroku
  - Rodar um hello world no heroku (Guilherme)
  - Decidir um template para o site (Guilherme e Victor)
- O usuário pode criar um cadastro
  - Criar tela de cadastro e de login (Guilherme e Victor)

### Testes
Durante a 1ª sprint foram criados testes unitários para verificar alterações no layout da aplicação, o principal objetivo foi garantir que mudanças de layout não removam elementos necessários para o funcionamento da página. Os testes foram distribuidos nas seguintes classes:

- HomePageTest
- LoginTest
- SignupTest

Cada classe é responsável por testar uma página da aplicação, de forma que os testes podem ser ampliados com facilidade nas implementações futuras. Por fim, os testes apresentaram uma cobertura total de 85%.

### Retrospectiva
- O que deu certo no sprint? Quais foram os pontos mais positivos?
  - R.: Conseguimos criar um fluxo para subir a aplicação no Heroku e preparamos o ambiente para execução de testes, além de criarmos alguns testes iniciais.
- O que deu errado no sprint? Onde e o que podemos melhorar?
  - R.: Dificuldade de criação e manutenção da aplicação Django, bem como problemas ao subir a aplicação para o Heroku.

## Sprint 2

### Histórias e tarefas
- O usuário pode criar/editar cartões
  - Tela para criação de cartão (Guilherme)
  - Tela para edição de cartão (Victor)
  - Criar métodos CRUD para os dados do cartão (Guilherme)
  - Criar testes de validação do cartão (Victor)
- Um usuário pode pesquisar outros cartões
  - Criar tela de pesquisa de cartões (Victor)
- Um usuário pode marcar e visualizar cartões como favoritos
  - Criar tela para visualização de cartões (Victor)
  - Criar tela para visualizar um cartão (Victor)
  - Compartilhar cartão via link (Victor e Guilherme)

### Testes
Durante a 2ª sprint foram criados testes unitários para verificar a criação de cartões, bem como testes de integração para verificar a edição de cartões e o funcionamento do sistema. Além disso, foi criado um teste fim-a-fim para exercitar o sistema por completo. Os testes foram distribuidos nas seguintes classes:

- CardTests
- IntegrationTests

Cada classe é responsável por testar os respectivos aspectos citados no parágrafo acima. Por fim, os testes apresentaram uma cobertura total de 87%.

### Retrospectiva
- O que deu certo no sprint? Quais foram os pontos mais positivos?
  - R.: Conseguimos criar a principal função do sistema, que é a de criação e edição de cartões, além de ser possível compartilhá-los por meio do link.
- O que deu errado no sprint? Onde e o que podemos melhorar?
  - R.: Gostaríamos de ter finalizado todas as histórias para fazer uma sprint 100% de produção na Sprint 3, porém não foi possível. Sendo assim, parte das histórias ainda será implementada na Sprint 3.

## Sprint 3

### Histórias e Tarefas
- Um usuário pode marcar e visualizar cartões como favoritos 
  -  Criar botão para marcar cartão como favorito (Victor)
  -  Criar tela para ver cartões favoritos (Victor)
  -  Criar métodos CRUD para cartões favoritos (Victor)
- Um usuário pode pesquisar outros cartões 
  -  Criar métodos CRUD (Guilherme)
- Um usuário pode criar, ver, editar e apagar seu cadastro
  -  Editar os dados do cadastro (Guilherme)
  -  Deletar conta (Guilherme)
- Testes com usuários (Wanderson)

### Testes
Durante a 3a sprint, foram criados testes de unidade e de integração para cada uma das novas funcionalidades implementadas, localizando-se nas classes CardTests e IntegrationTests, alcançando, dessa forma, a marca de 91% de cobertura. Além disso, foram conduzidos testes com usuários reais. 

### Retrospectiva
- O que deu certo no sprint? Quais foram os pontos mais positivos?
  - R.: Conseguimos concluir todas as funcionalidades propostas para o sistema e conduzir testes com usuários reais.
- O que deu errado no sprint? Onde e o que podemos melhorar?
  - R.: Gostariamos de ter tido mais tempo para melhorar o visual de algumas páginas html.
