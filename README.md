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

### Testes com usuários
Após o desenvolvimento, foram conduzidos 4 testes com usuários reais. Todos os testes foram realizados com o usuário utilizando o compartilhamento de tela do google meet para o acompanhamento das tarefas. 3 dos testes foram feitos no computador do usuário, e neles foi pedido que ele habilitasse a câmera para que o aplicador pudesse ver as expressões do usuário durante o teste. Um deles foi realizado utilizando o celular do usuário, e nesse teste não houve o acompanhamento da câmera.
Cada usuário recebeu 3 tarefas que possuem como objetivo simular as ações mais comuns que serão executadas na plataforma. A primeira tarefa tinha como objetivo mapear o primeiro contato do usuário na plataforma, nela foi pedido que ele criasse uma conta e realizasse o login no site. Após isso, foi pedido que ele alterasse alguma informação do perfil e salvasse essa alteração.
A segunda tarefa teve como foco os cartões do usuário, nela foi pedido que ele criasse um cartão. Após isso, foi pedido que o usuário editasse ele e o excluísse em sequência. O último teste teve como foco a busca por cartões de outro usuário, nessa tarefa foi pedido que o ele buscasse por um cartão específico na plataforma e para favoritar esse cartão. Em sequência, o usuário deveria entrar na aba de 'Cartões Favoritos', achar o cartão que ele favoritou e desfavoritar ele.
Ao final dos testes, foi pedido para o usuário um feedback sobre os pontos positivos e negativos da sua interação com o sistema. As listas abaixo apresentam um compilado dos principais pontos informados por eles:
- ##### Pontos Positivos
    - Os usuários não tiveram problemas durante a atualização dos dados presentes no perfil do atleta, porém utilizar o nome do usuário no menu ao invés de 'meu perfil' no menu pode não ser intuitivo para usuários mais leigos
    - Não houve dificuldades para criar um novo cartão visto que era explícito no menu onde que ele é criado
    - Foi bem intuitivo para os usuários alterarem e deletarem um cartão, visto que existem botões explicitando cada ação
    - Os usuários não tiveram problemas para adicionar e remover um card dos seus favoritos porque existem botões explícitos para cada uma dessas funções.

- ##### Pontos Negativos
    - A página inicial do site não é muito intuitiva pois a tela inicial já informa que nenhum cartão foi encontrado
    - Os usuários tiveram dificuldades para achar o cadastro porque ele só aparece após clicar em login no menu à direita
    - Alguns usuários tiveram problemas durante o cadastro pois o sistema exige que seja informada uma senha forte, porém não exibe um erro caso a senha seja fraca, somente a página que é recarregada o que gerou dúvidas no cadastro
    - O visual da aplicação não é muito atrativo dada a simplicidade dos layouts utilizados após o usuário estar logado na aplicação, além disso o layout não é responsivo o que gerou uma má experiência para o usuário mobile
    - Houve uma saturação do menu à direita, as principais funções ficaram 'escondidas' dentro dele quando elas poderiam ter sido espalhadas pela tela
    - A foto é redimensionada perdendo suas proporções ao ser inserida no cartão, isso pode levar a experiências negativas em casos que ela é importante como para uma modelo por exemplo

Após a conclusão dos testes, ficou claro que o sistema não apresentou erros graves durante o uso. Porém as principais críticas foram relacionadas a parte de design e de experiência do usuário. Por isso, essa plataforma funcionou bem como um MVP para apresentar a ideia para possíveis usuários. Ainda assim, todos os pontos negativos devem ser levados em consideração antes do sistema ser finalizado.

### Retrospectiva
- O que deu certo no sprint? Quais foram os pontos mais positivos?
  - R.: Conseguimos concluir todas as funcionalidades propostas para o sistema e conduzir testes com usuários reais.
- O que deu errado no sprint? Onde e o que podemos melhorar?
  - R.: Gostariamos de ter tido mais tempo para melhorar o visual de algumas páginas html.
