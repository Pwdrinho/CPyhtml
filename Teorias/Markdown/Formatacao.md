# Formatações em Markdown

Este documento apresenta todos os principais recursos e formatações suportadas em Markdown, conforme a documentação oficial e extensões comuns (como GitHub Flavored Markdown).

## Títulos
```markdown
# Título 1
## Título 2
### Título 3
#### Título 4
##### Título 5
###### Título 6
```

## Ênfase de Texto

*Itálico* 

**Negrito**

~~Tachado~~ 

<u>Sublinhado</u>

```markdown
*Itálico* ou _Itálico_
**Negrito** ou __Negrito__
~~Tachado~~
<u>Sublinhado</u>
__Sublinhado
```

## Listas
### Listas Ordenadas
```markdown
1. Primeiro item
2. Segundo item
3. Terceiro item
```

### Listas Não Ordenadas
```markdown
- Item
- Item
- Item
```
Ou:
```markdown
* Item
* Item
* Item
```

### Listas Aninhadas
```markdown
- Item 1
  - Subitem 1.1
  - Subitem 1.2
- Item 2
```

## Links
```markdown
[Texto do Link](https://www.exemplo.com)
[Texto do Link com título](https://www.exemplo.com "Título")
```

## Imagens
```markdown
![Texto Alternativo](https://www.exemplo.com/imagem.png)
![Texto com Título](https://www.exemplo.com/imagem.png "Título da Imagem")
```

## Citações (Blockquotes)
```markdown
> Este é um bloco de citação.
>> Citação aninhada.
```

## Código
### Código Inline
```markdown
Use `código` para inline.
```

### Bloco de Código
```markdown
```
Bloco de código simples
```
```

### Bloco de Código com Linguagem
```markdown
```python
print("Olá, Mundo!")
```
```

## Tabelas
```markdown
| Cabeçalho 1 | Cabeçalho 2 |
|-------------|-------------|
| Linha 1     | Conteúdo    |
| Linha 2     | Conteúdo    |
```

### Alinhamento em Tabelas
```markdown
| Esquerda | Centro  | Direita |
|:---------|:-------:|--------:|
| A        | B       | C       |
```

## Separadores
```markdown
---
```
Ou:
```markdown
***
```
Ou:
```markdown
___
```

## Checklists
```markdown
- [ ] Tarefa pendente
- [x] Tarefa concluída
```

## Escapes
```markdown
\*Este texto não estará em itálico\*
```

## Comentários
```markdown
<!-- Comentário que não será exibido -->
```

## HTML Embutido
O Markdown permite a inserção de HTML direto:
```markdown
<b>Texto em negrito usando HTML</b>
<i>Texto em itálico usando HTML</i>
```

## Emojis (GitHub Flavored Markdown)
```markdown
:smile: :rocket: :thumbsup:
```

## Menções e Referências (GitHub)
```markdown
@usuário — Menciona um usuário
#123 — Referência a uma issue ou pull request
```

## Task Lists Avançadas (GitHub)
```markdown
- [ ] Tarefa 1
  - [x] Subtarefa completa
  - [ ] Subtarefa pendente
```

---
Este documento lista todas as formatações fundamentais do Markdown, incluindo extensões populares como GFM (GitHub Flavored Markdown), permitindo a criação de documentos claros, organizados e poderosos! 🚀