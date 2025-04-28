# Estrutura de Página em HTML

A estrutura de uma página em HTML é composta por diversos elementos que organizam o conteúdo e a disposição visual do site. O uso correto desses elementos ajuda na acessibilidade, semântica e responsividade.

## Principais Elementos de Estrutura

### `<div>`
O elemento `<div>` é um contêiner genérico usado para agrupar e estruturar elementos dentro da página sem adicionar significado semântico.

### `<header>`
Define a seção de cabeçalho da página ou de um bloco de conteúdo.

### `<nav>`
Define um conjunto de links de navegação.

### `<main>`
Define o conteúdo principal do documento. Deve ser único por página.

### `<section>`
Agrupa conteúdos tematicamente relacionados dentro da página.

### `<article>`
Define um conteúdo independente e autossuficiente, como postagens de blog ou notícias.

### `<aside>`
Define conteúdos complementares, como barras laterais, anúncios ou links adicionais.

### `<footer>`
Define o rodapé do documento ou de uma seção.

---

### Exemplo de estrutura completa:
```html
<head>
    <title>Minha Página</title>
</head>
<body>
    <header>
        <h1>Meu Site</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Sobre</a></li>
                <li><a href="#">Contato</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section>
            <h2>Seção Principal</h2>
            <article>
                <h3>Artigo Importante</h3>
                <p>Este é um exemplo de artigo dentro de uma seção principal.</p>
            </article>
        </section>
        
        <aside>
            <h3>Conteúdo Relacionado</h3>
            <p>Links e informações adicionais.</p>
        </aside>
    </main>
    
    <footer>
        <p>&copy; 2025 Meu Site. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
```

---
Esses são os principais elementos utilizados para estruturar uma página em HTML de maneira organizada e semântica. 🚀