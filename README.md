# ICard

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
