# Introdução ao LaTeX

Principais tópicos sobre LaTeX

### Terminação do arquivo
todo arquivo em LaTeX deve conter no final o .tex

*ex*: `main.tex`

---
### Comentários
`% This line here is a comment. It will not be typeset in the document.`

---
### Bold, Italics and Underlining

- **Bold**: text typeset using the `\textbf{...}`
- ***Italics***: text typeset using the `\textit{...}`
- **<u>Underline</u>** text typeset to underline `\underline{...}`

---
### Adicionar Imagens
 3 maneiras de fazer isso:
1. Use the Insert Figure button(The Insert Figure button on the editor toolbar), located on the editor toolbar, to insert an image into Visual Editor or Code Editor.
2. Copy and paste an image into Visual Editor or Code Editor.
3. Use Code Editor to write LaTeX code that inserts a graphic.
```Latex
\usepackage{graphicx} %LaTeX package to import graphics
\graphicspath{{images/}} %configuring the graphicx package para puxar imagem dentro de uma pasta
```

##### Obs:
Geralmente, deve-se omitir as extensões do arquivo, tampouco utilizar espaços no nome do arquivo

#### Legendas, Rótulos e Referências

As imagens podem ser legendadas, rotuladas e referenciadas por meio do figureambiente, conforme mostrado abaixo:

```Latex
\begin { figure } [h]
     \centering 
    \includegraphics [width=0.75\textwidth] { mesh } 
    \caption { Um belo gráfico. } 
    \label { fig:mesh1 } 
\end { figure }
  
Como você pode ver na figura \ref { fig:mesh1 } , a função cresce perto da origem. Este exemplo está na página \pageref { fig:mesh1 }.
```

--- 

### Lists

#### Unordered

#### Ordered

---

### Math on LaTeX

#### inline

#### Display

---

### Resumo (Abstract)

---

### Parágrafos e novas linhas

---

### Capítulos e Seções

---

### Tabelas

#### Bordas

#### Legendas, Rótulos e Referências

#### Índices

---