# Tipos de Input em HTML

O elemento `<input>` em HTML possui diversos tipos que permitem a entrada de diferentes tipos de dados pelos usuários. No total, existem 22 tipos diferentes.

## Tipos de Input e suas funções

### Entrada de Texto
- **`type="text"`** → Define um campo de *texto* de uma linha (padrão).
- **`type="email"`** → Define um campo de *entrada de e-mail* (valida formato de e-mail).
- **`type="password"`** → Define um campo de *senha* (oculta os caracteres digitados).
- **`type="tel"`** → Define um campo de *entrada de telefone*.
- **`type="number"`** → Define um campo para inserir um *número* (permite setas para incremento/decremento).
- **`type="search"`** → Define um *campo de pesquisa* (visual semelhante ao campo de busca de navegadores).
- **`type="url"`** → Define um campo de *entrada de URL* (valida se o valor inserido é uma URL válida).

### Upload e Arquivos
- **`type="file"`** → Define um campo de *envio de arquivo* (permite seleção de arquivos).
- **`type="hidden"`** → Define um campo *oculto* (não visível para o usuário, mas enviado no formulário).

### Botões
- **`type="button"`** → Define um *botão clicável* sem funcionalidade específica.
- **`type="reset"`** → Define um *botão de redefinição* (restaura os valores do formulário ao estado inicial).
- **`type="submit"`** → Define um *botão de envio* para submeter o formulário ao servidor.

### Seleção e Escolha
- **`type="radio"`** → Define um *botão de opção* (permite *seleção única* dentro de um grupo).
- **`type="checkbox"`** → Define uma *caixa de seleção* (permite *seleção múltipla*).
- **`type="range"`** → Define um *controle deslizante para inserir um número dentro de um intervalo*.

### Elementos Visuais e Específicos
- **`type="image"`** → Define um *botão de imagem* (pode ser usado para enviar formulários ao clicar na imagem).
- **`type="color"`** → Define um *controle para selecionar uma cor* (abre um seletor de cores).

### Datas e Tempo
- **`type="month"`** → Define um *controle para inserir um mês e ano*.
- **`type="date"`** → Define um *controle para inserir uma data (sem hora)*.
- **`type="datetime-local"`** → Define um *controle para inserir uma data e hora*.
- **`type="week"`** → Define um *controle para inserir uma semana e ano*.
- **`type="time"`** → Define um *controle para inserir uma hora*.

## Elemento `<form>`
O elemento `<form>` é utilizado para criar formulários em HTML, permitindo que os usuários insiram e enviem dados. 

### Atributos importantes do `<form>`
- **`action`** → Define o destino para onde os dados do formulário serão enviados.
- **`method`** → Define o método HTTP de envio (`GET` ou `POST`).
- **`enctype`** → Define o tipo de codificação dos dados (importante para uploads de arquivos).

### Exemplo de um formulário simples
```html
<form action="/submit" method="POST">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" required>
    
    <label for="email">E-mail:</label>
    <input type="email" id="email" name="email" required>
    
    <input type="submit" value="Enviar">
</form>
```

Esse exemplo cria um formulário com campos para nome e e-mail e um botão de envio.

---
Esses são os principais tipos de input disponíveis no HTML para diferentes finalidades. 🚀