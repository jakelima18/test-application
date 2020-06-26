# Teste Flask + MongoDB
Os desenvolvedores da empresa XPTO estão testando uma nova API em python e para agilizar o testes foi solicitado que seja criado uma esteira de integração e deploy das branchs `master` e `desenvolvimento`. Abaixo segue os detalhes do projeto:
 - Desenvolvido para utilizar o Python 3.7
 - Compatível com a versão 4.2 do MongoDB
 - A aplicação expõe a porta 5000 por padrão
 - A configuração do banco de dados fica no arquivo `config.py`
 - A aplicação inicia com o comando `python run-app.py`

# Qual é sua missão?
A empresa XPTO utiliza Jenkins como ferramenta de integração e kubernetes para execução dos microserviços. Sua missão é criar uma pipeline utilizando `Jenkinsfile` para instalar as dependências e efetuar o deploy em um cluster Kubernetes.

# Como deve ser entregue?
Crie um fork deste projeto, faça todas as alterações e crie todos os arquivos que julgar necessário. Quanto estiver pronto, compartilhe a URL do repositório.

Por se tratar de um projeto novo, podem haver pontos que precisam ser melhorados antes ir para produção. Caso os encontre, adicione no `README.md` do projeto explicando o motivo da mudanca. É sempre bom direcionar os desenvolvedores :).

# Solução:
Foi implantado o Jenkins como um container dentro do cluster de Kubernetes. Utilizei o chart do Helm para fazer o deploy do Jenkins. Criei o dockerfile da aplicação e os manifestos do Kubernetes para o mongodb e para o backend. A unica modificação que fiz no codigo da aplicação foi alterar as interfaces de rede em que a aplicação executa para que pudessemos acessa-la externamente. E recomendavel alterar a forma de string de conexão para o banco de dados para que possamos armazenar essas informações em secrets do Kubernetes e desacoplar da imagem. Foi criado um namespace para o ambiente de produção e um para o ambiente de desenvolvimento. A cada nova alteração enviada para o repositorio, o processo de CI/CD é disparado. O build da imagem docker é realizado e feito o envio para a minha conta do Dockerhub e apos isso a nova imagem é aplicada para o namespace correto de acordo com o nome do branch para qual foi enviado a alteração. O deploy é condicional. Se o alteração for enviada para o branch develop, a imagem é alterada no namespace develop. Se a alteração for enviada para o branch master, a imagem é alterada no namespace production.
