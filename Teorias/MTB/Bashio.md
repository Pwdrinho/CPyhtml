# Comandos de Entrada e Saída no Bash (I/O)

Este documento apresenta os principais comandos e operadores de entrada e saída utilizados em scripts Bash, com breves explicações sobre cada um deles.

## Redirecionamento de Saída
- `>` — Redireciona a saída padrão para um arquivo (sobrescreve).
- `>>` — Redireciona a saída padrão para um arquivo (anexa).

## Redirecionamento de Entrada
- `<` — Usa o conteúdo de um arquivo como entrada de um comando.

## Redirecionamento de Erro
- `2>` — Redireciona a saída de erro para um arquivo (sobrescreve).
- `2>>` — Redireciona a saída de erro para um arquivo (anexa).

## Redirecionamento Combinado
- `&>` — Redireciona saída padrão e de erro para o mesmo arquivo (sobrescreve).
- `&>>` — Redireciona saída padrão e de erro para o mesmo arquivo (anexa).

## Descarte de Saída
- `> /dev/null` — Descarta a saída padrão.
- `2> /dev/null` — Descarta a saída de erro.
- `&> /dev/null` — Descarta tanto a saída padrão quanto a saída de erro.

## Here Document e Here String
- `<<` — Cria um bloco de entrada multi-linha (here document).
- `<<<` — Fornece uma string como entrada direta (here string).

## Manipulação de Texto
- `cat` — Exibe o conteúdo de arquivos.
- `tac` — Exibe o conteúdo de arquivos em ordem reversa.
- `head` — Mostra as primeiras linhas de um arquivo.
- `tail` — Mostra as últimas linhas de um arquivo.
- `cut` — Extrai seções de texto por delimitadores.
- `tr` — Substitui ou remove caracteres.
- `sort` — Ordena linhas de texto.
- `uniq` — Remove linhas duplicadas consecutivas.
- `wc` — Conta linhas, palavras e caracteres.
- `nl` — Numera as linhas de um arquivo.
- `paste` — Une linhas de arquivos lado a lado.
- `tee` — Redireciona a saída para um arquivo e para o terminal simultaneamente.
- `awk` — Linguagem para manipulação e análise de dados estruturados.
- `sed` — Editor de fluxo para buscar, substituir e editar texto de forma não interativa.

## Busca e Filtro
- `grep` — Busca padrões de texto em arquivos.
- `egrep` — Versão estendida do `grep` com suporte a expressões regulares avançadas.
- `fgrep` — Versão do `grep` que busca texto literal.
- `find` — Localiza arquivos e diretórios no sistema.
- `xargs` — Constrói comandos a partir da entrada padrão.
- `locate` — Busca arquivos rapidamente usando um banco de dados indexado.

## Entrada Interativa
- `read` — Lê entrada do usuário ou de arquivos.
- `select` — Cria menus interativos a partir de opções.

## Manipulação de Arquivos
- `cp` — Copia arquivos ou diretórios.
- `mv` — Move ou renomeia arquivos e diretórios.
- `rm` — Remove arquivos e diretórios.
- `touch` — Cria arquivos vazios ou atualiza a data de modificação de arquivos.
- `mkdir` — Cria novos diretórios.
- `rmdir` — Remove diretórios vazios.
- `basename` — Extrai o nome do arquivo de um caminho.
- `dirname` — Extrai o diretório de um caminho.
- `stat` — Exibe informações detalhadas sobre arquivos.

## Comandos de Rede
- `curl` — Realiza requisições para URLs (*HTTP, FTP, etc.*).
- `wget` — Baixa arquivos da internet.
- `scp` — Copia arquivos entre sistemas via SSH.
- `ssh` — Conecta a máquinas remotamente usando SSH.
- `ftp` — Cliente de transferência de arquivos via FTP.
- `rsync` — Sincroniza arquivos e diretórios entre sistemas.

## Execução de Scripts e Processos
- `sh` — Executa comandos em uma nova shell.
- `bash` — Inicia uma nova sessão Bash ou executa scripts `.sh`.
- `ps` — Exibe os processos em execução.
- `jobs` — Lista os processos em segundo plano.
- `bg` — Coloca processos suspensos em segundo plano.
- `fg` — Traz processos para o primeiro plano.
- `kill` — Envia sinais para processos.
- `killall` — Envia sinais para todos os processos com o mesmo nome.
- `nohup` — Executa comandos ignorando hangups, permitindo que continuem após logout.
- `disown` — Remove um processo da lista de trabalhos da shell atual.

## Permissões e Gerenciamento de Pacotes
- `alias` — Define atalhos personalizados para comandos.
- `chmod` — Altera permissões de arquivos e diretórios.
- `chown` — Altera o proprietário e o grupo de arquivos.
- `dpkg` — Gerencia pacotes `.deb` em sistemas baseados em Debian.
- `apt` — Gerenciador de pacotes de alto nível para sistemas Debian/Ubuntu.
- `yum` — Gerenciador de pacotes para sistemas Red Hat/CentOS.
- `pacman` — Gerenciador de pacotes para sistemas Arch Linux.

## Pipes e Substituições
- `|` — Conecta a saída de um comando à entrada de outro (pipe).
- `|&` — Conecta a saída padrão e de erro de um comando à entrada de outro.
- `$(comando)` — Substitui o comando pelo seu resultado (command substitution).
- `` `comando` `` — Forma antiga de substituição de comando.
- `<(comando)` — Redireciona a saída de um comando como se fosse um arquivo (process substitution).
- `>(comando)` — Redireciona a saída de um comando para a entrada de outro.

## Manipulação de Descritores de Arquivo
- `exec` — Redireciona descritores de arquivos ou substitui o processo atual.
- `exec 3>arquivo.txt` — Abre o descritor de saída 3 para escrever no arquivo.
- `exec 4<entrada.txt` — Abre o descritor de entrada 4 para ler de um arquivo.
- `>&n` — Redireciona a saída para outro descritor de arquivo.
- `<&n` — Redireciona a entrada a partir de outro descritor de arquivo.

---
Este documento cobre um conjunto abrangente e atualizado de comandos e operadores usados para entrada e saída no Bash, essenciais para scripts, manipulação de arquivos, automação de tarefas e administração de sistemas Linux. 🚀