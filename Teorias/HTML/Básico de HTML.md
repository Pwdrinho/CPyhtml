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

## Títulos e Texto

- `<h1></h1>` → Define um cabeçalho de nível 1 (o maior).
- `<h6></h6>` → Define um cabeçalho de nível 6 (o menor).
- `<p></p>` → Define um parágrafo.
- `<b></b>` → Deixa o texto em **negrito**.
- `<i></i>` → Deixa o texto em *itálico*.

## Listas

- `<ul></ul>` → Define uma **lista não ordenada** (bullet points).
- `<ol></ol>` → Define uma **lista ordenada** (numerada).
- `<li></li>` → Define um **item** dentro de uma lista.

## Links e Navegação

- `<a href="URL"></a>` → Define um **link** para uma URL externa ou interna.

## Tabelas

- `<table></table>` → Define uma **tabela**.
- `<tr></tr>` → Define uma **linha** da tabela.
- `<th></th>` → Define um **cabeçalho de coluna**.
- `<td></td>` → Define uma **célula de dados**.

## Formulários

- `<form></form>` → Define um formulário.
- `<input type="text">` → Campo de entrada de texto.
- `<input type="email">` → Campo de entrada de e-mail.
- `<input type="submit">` → Botão de envio do formulário.

## Imagens e Quebras de Linha

- `<img src="url"/>` → Define uma **imagem** e não requer uma tag de fechamento.
  - O atributo `src` é obrigatório e define o **caminho da imagem**, podendo ser uma **URL externa** (exemplo: `https://exemplo.com/imagem.jpg`) ou um **arquivo local** (exemplo: `imagem.jpg`).
  - Exemplo de uso:
    ```html
    <img src="https://exemplo.com/imagem.jpg" alt="Descrição da imagem">
    ```
  - O atributo `alt` é recomendado para descrever a imagem para leitores de tela e quando a imagem não pode ser carregada.

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