# Comandos Básicos para Construção de um HTML

## Criando um Esqueleto HTML5

- `! + TAB` → Cria um esqueleto de um documento HTML5.
- `html:5` → Também cria um esqueleto de um documento HTML5.

## Estrutura Básica

- `<html></html>` → Define o início e o fim de um documento HTML.
- `<head></head>` → Contém metadados do documento.
- `<body></body>` → Contém o conteúdo visível da página.
- `<tag>` → **Tag de abertura**.
- `</tag>` → **Tag de fechamento**.

## Metatags

  Responsáveis por modificar a apresentação ou o comportamento do restante do documento.

- `<base>` →
- `<link>` → Especifica relacionamento entre o documento e um recurso externo. "stylesheet" ou estabelecer ícones do site. pode tanto ser usado no `<head>` como no `<body>`.
```html
<link href="main.css" rel="stylesheet" />
```
- `<script>` →
- `<noscript>` →
- `<style>` →
- `<template>` →
- `<title> </title>` →
- `<meta>` → Representa os elementos de *metadados* que não podem ser representados por outros *elementos meta-relacionados* como os citado acima.

## Títulos e Texto

- `<h1> </h1>` → Define um cabeçalho de nível 1 (o maior).
- `<h6> </h6>` → Define um cabeçalho de nível 6 (o menor).
- `<p> </p>` → Define um parágrafo.
- `<b> </b>` → Deixa o texto em **negrito**.
- `<i> </i>` → Deixa o texto em *itálico*.
- `<em> </em>` →

## Listas

- `<ul> </ul>` → Define uma **lista não ordenada** (bullet points).
- `<ol> </ol>` → Define uma **lista ordenada** (numerada).
- `<li> </li>` → Define um **item** dentro de uma lista.

## Links e Atributos

- `<a href="URL"> </a>` → Define um **link** para uma URL externa ou interna.

- O atributo `href` é utilizado para indicar o endereço URL da página ou recurso para onde o link vai.

- O atributo `rel` especifica o relacionamento entre o documento atual e outro documento ou recurso ao qual ele está vinculado.

- O atributo `src` é obrigatório e define o **caminho da imagem**, podendo ser uma **URL externa** (exemplo: `https://exemplo.com/imagem.jpg`) ou um **arquivo local** (exemplo: `../../imagens/imagem.jpg`).

- O atributo `alt` é recomendado para descrever a imagem para leitores de tela e quando a imagem não pode ser carregada.

- O atributo `sizes` refere-se ao tamanho dos recursos ou elementos como `<img>`

- O atributo `type` define o tipo de elemento ou de conteúdo como os que podem ser observados em: <a href= ../HTML/InputTypes.md> Input Types</a>

- O atributo `as`

- O atributo `media`

- O atributo `crossorigin`

### Atributos Metadados

- O atributo`charset` declara a codificação de caracteres do documento correspondendo ao *ASCII* `"utf-8"` para html5.

- O atributo`content`contém o valor do atributo `http-equiv` ou `name`

- O atributo`http-equiv`define uma diretiva pragma:
  - O atributo`content-security-policy` define uma *política de conteúdo*, geralmente especificam origens de servidor e endpoint de scripts.
  <em obs:> ajuda a proteger contra ataques de cross-site-scripting</em>
  - O atributo`content-type` 
  - O atributo`default-style`
  - O atributo`x-ua-compatible`
  - O atributo`refresh`


## Tabelas

- `<table> </table>` → Define uma **tabela**.
- `<tr> </tr>` → Define uma **linha** da tabela.
- `<th> </th>` → Define um **cabeçalho de coluna**.
- `<td> </td>` → Define uma **célula de dados**.

## Formulários

- `<form> </form>` → Define um formulário.
- `<input type="text">` → Campo de entrada de texto.
- `<input type="email">` → Campo de entrada de e-mail.
- `<input type="submit">` → Botão de envio do formulário.

## Imagens e Quebras de Linha

- `<img src="url"/>` → Define uma **imagem** e não requer uma tag de fechamento.

  - Exemplo de uso:

    ```html
    <img src="https://exemplo.com/imagem.jpg" alt="Descrição da imagem">
    ```

- `<br>` → Define uma **quebra de linha** e não requer uma tag de fechamento.
  - É usado dentro de parágrafos ou blocos de texto para inserir quebras de linha sem iniciar um novo parágrafo.
  - Exemplo de uso:

    ```html
    <p>Esta é a primeira linha.<br>Esta é a segunda linha.</p>
    ```

- `<hr>` → Define uma **linha horizontal** e não requer uma tag de fechamento.
  - Pode ser usada para separar seções de conteúdo.
  - Exemplo de uso:

    ```html
    <p>Texto acima da linha.</p>
    <hr>
    <p>Texto abaixo da linha.</p>
    ```

---
Esses são os principais elementos do HTML para começar a construir páginas web. 🚀