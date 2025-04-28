# Comandos Essenciais do Editor Vim

Este documento lista os principais comandos do editor Vim, baseados em sua documentação oficial, com breves descrições.

## Modos de Operação
- `Esc` — Voltar ao modo normal.
- `i` — Inserir texto antes do cursor (modo de inserção).
- `I` — Inserir no início da linha.
- `a` — Inserir texto após o cursor.
- `A` — Inserir no final da linha.
- `o` — Nova linha abaixo.
- `O` — Nova linha acima.
- `v` — Iniciar seleção visual.
- `V` — Selecionar linha inteira (modo visual linha).
- `Ctrl+v` — Seleção em bloco (modo visual bloco).

## Movimentação
- `h` — Move cursor para a esquerda.
- `l` — Move cursor para a direita.
- `j` — Move cursor para baixo.
- `k` — Move cursor para cima.
- `0` — Início da linha.
- `^` — Primeiro caractere não vazio da linha.
- `$` — Fim da linha.
- `w` — Próxima palavra.
- `b` — Palavra anterior.
- `gg` — Início do arquivo.
- `G` — Fim do arquivo.
- `:{n}` — Ir para linha n.

## Edição de Texto
- `x` — Apagar caractere sob o cursor.
- `dd` — Apagar (cortar) linha inteira.
- `yy` — Copiar linha inteira.
- `p` — Colar abaixo do cursor.
- `P` — Colar acima do cursor.
- `u` — Desfazer última alteração.
- `Ctrl+r` — Refazer última alteração.
- `r{char}` — Substituir caractere sob o cursor.
- `~` — Alternar maiúsculo/minúsculo do caractere.
- `J` — Juntar linha atual com a próxima.

## Busca e Substituição
- `/texto` — Buscar "texto" para frente.
- `?texto` — Buscar "texto" para trás.
- `n` — Próxima ocorrência.
- `N` — Ocorrência anterior.
- `:%s/antigo/novo/g` — Substituir todos "antigo" por "novo" no arquivo.

## Arquivos e Buffers
- `:w` — Salvar arquivo.
- `:w nome.txt` — Salvar como novo arquivo.
- `:q` — Sair.
- `:q!` — Sair sem salvar.
- `:wq` — Salvar e sair.
- `:e nome.txt` — Abrir arquivo.
- `:bnext` — Próximo buffer.
- `:bprev` — Buffer anterior.

## Janelas (Splits)
- `:split` — Dividir tela horizontalmente.
- `:vsplit` — Dividir tela verticalmente.
- `Ctrl+w` depois `h/j/k/l` — Mover entre janelas.
- `Ctrl+w` depois `c` — Fechar janela.

## Marcação e Navegação
- `m{a-z}` — Marcar posição.
- `'a` — Voltar para a marca "a".
- `` `a`` — Voltar exatamente à posição marcada "a".

## Outras Ações
- `:set number` — Mostrar números de linha.
- `:set nonumber` — Ocultar números de linha.
- `:syntax on` — Ativar realce de sintaxe.
- `:syntax off` — Desativar realce de sintaxe.
- `:noh` — Remover realce de buscas.
- `:!comando` — Executar comando do sistema.

---
Este documento resume os comandos fundamentais do Vim para navegação, edição e gerenciamento de arquivos de forma rápida e eficiente no terminal Linux! 🚀