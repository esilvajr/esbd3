## Activities

#### Adapter

Você trabalha com um sistema cujo código cliente process dados no formato JSON. Entretanto, o fornecedor da API agora não fornece mais dados nesse formato, mas sim em .doc. Por razões diversas, você não pode mais alterar o código cliente….  E agora ??? o que fazer ?

[Resolução](https://github.com/esilvajr/esbd3/blob/master/activities/adapter.py)

#### Facade
Faz parte de um sistema legado de universidade ser responsável por gerar planos de ensino para os cursos.
Esta parte não foi bem projetada ...
A geração de um plano de ensino envolve a obtenção de dados de professores, calendários, aulas e disciplinas didáticas.
Como você refatoraria isso para que a funcionalidade de geração de planos de ensino pudesse ser mais modular e evidente no código?

[Resolução](https://github.com/esilvajr/esbd3/blob/master/activities/facade.py)


#### Factory Method
Agora que sabemos como é a pattern do Factory Method. Vamos então utilizá-la para criar um algoritmo que implemente fábricas para criar objetos que simulam o pacote office.
Cada aplicativo (word, excel, powerpoint e ms project) deve ter uma fábrica para criar sua instância.
No caso do Word e do Excel o usuário pode escolher entre as versões doc e xls ou docx e xlsx.

[Resolução](https://github.com/esilvajr/esbd3/blob/master/activities/factory_method.py)


#### Observer
Um cliente está interessado em um produto em particular, um telefone Iphone que é novidade e em breve estará disponivel. Crie um sistema que observe o estado de disponibilidade dos telefones e que seja possivel o cliente se inscrever para ser notificado.
Como faríamos essa implementação?

[Resolução](https://github.com/esilvajr/esbd3/blob/master/activities/observer.py)
