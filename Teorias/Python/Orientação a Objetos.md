# Orientação à Objetos

O desenvolvimento orientado a objetos, facilita muito a compreensão de alguns conceitos, torna a programação mais simples de ser compreendida e facilita o trabalho em equipe!

Projetos desenvolvidos utilizando a Orientação a Objetos são mais *estáveis, de fácil manutenção e sua reutilização é mais simples*.

#### Vantagens
- Reutilização (criação de bibliotecas);
- Polimento do código;
- Simplificação com representações mais claras;
- Manutenção.

## Classes e Objetos

### Classe
É um modelo para uma objeto. Feito por meio de **Instanciação**. ("molde" para os objetos)
> Pense em uma classe como um esboço (**protótipo**) de uma casa. Ele **contém todos os detalhes** sobre os pisos, portas, janelas etc. Com base nessas descrições, podemos construir a casa. Nesse exemplo a **casa é o objeto**.

É possivel **criar muitos objetos de uma classe** que também pode ser chamado de **instância** de uma classe.
- `class` palavra-chave para criação de uma classe.
- `Docstring` a primeira *string* dentro da classe que apresenta uma breve descrição da classe.

```python
class Casa:
    "Isto é uma docstring. Eu a criei dentro da minha classe"
pass
```
Veja que uma classe cria um *namespace*, local onde todos os seus atributos são definidos. Os **atributos podem ser dados ou funções**. Há também atributos especiais que começam com sublinhados duplos: __.

Por exemplo, **__doc__** que nos dá a docstring dessa classe.

### Objeto
Um objeto é uma **coleção de dados(variáveis)** e **métodos(funções)** que atuam sobre esses dados comuns à classe.

Assim que é definida uma classe, um novo objeto de classe é criado com o mesmo nome. Esse objeto nos permite acessar os diferentes atributos, bem como instanciar novos objetos dessa classe.

```python
class Pessoa:
    
    "Isto é uma classe chamada Pessoa"

    idade = 15

    def saudacao(self):
        print("Olá Pessoas!")

pass

print(Pessoa.idade)
#Output: 15

print(Pessoa.saudacao)
# Output: <function Pessoa.saudacao> na prática: "Olá Pessoas!"

print(Pessoa.__doc__)
# Output: “Isto é uma classe nova chamada Pessoa”
```
Para criar um objeto é semelhante a **função**
```python
matheus = Pessoa()
```

## Conceitos

### Abstração
É o acesso às utilidades da classe, utilizando mensagens para acessar os recursos de uma classe.
> **Mensagem** chamada a um atributo, método ou função.

### Atributos
São as características (*propriedades*) do elemento que a classe representa. São as **declarações de variáveis** da classe

### Métodos
São as **ações da classe**, suas funções. Representam os estados e ações dos objetos quando instanciados.
*Ação do Objeto*

As funções de classe que começam com sublinhado duplo `__palavrareservada__` são chamadas de construtores, pois têm um significado especial.

- Método Contrutor: é utilizado para construir o objeto
``` python
class MinhaClasse:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.parâmetro2 = parâmetro2
        pass
```
O `__init__()` normalmente é utilizado para inicializar todas as variáveis, será chamado sempre que criarmos um objeto da classe.

O parâmetro obrigatório `self` exporta as características do objeto. (Todo método Python tem self como primeiro parâmetro.)



## Encapsulamento
Permite que os atributos sejam vistos somente nas classes onde foram declaradas, definido o **nível de acesso** de atributos, métodos ou funções.

## Relações

### Herança
Uma classe pode **herdar** atributos, métodos e/ou funções de outra classe.

### Polimorfismo