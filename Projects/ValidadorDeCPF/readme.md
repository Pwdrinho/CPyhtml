# Validador de CPF

Um algoritmo simples para validação de CPF (Cadastro de Pessoa Física), baseado no cálculo dos dígitos verificadores. O código foi desenvolvido com foco no aprendizado e aplicação de conceitos de **Orientação a Objetos**.

---

## 🔍 Como funciona a validação

A validação de um CPF se baseia nos **dois últimos dígitos**, chamados de **dígitos verificadores**. O processo consiste em:

1. Extrair os **9 primeiros dígitos** do CPF informado.
2. Calcular o **1º dígito verificador**.
3. Calcular o **2º dígito verificador**, agora incluindo o 1º.
4. Formar um novo CPF com os dois dígitos calculados.
5. Comparar o novo CPF com o original:
   - Se forem **iguais**, o CPF é **válido**.
   - Caso contrário, é **inválido**.

---

## 🧮 Cálculo dos dígitos verificadores

###  Primeiro dígito

1. Multiplicar os **9 primeiros dígitos** por uma sequência decrescente de **10 a 2**.  
2. Somar os resultados.
3. Calcular: `soma % 11`.
4. Subtrair o resultado de **11**: `11 - (soma % 11)`.
5. Se o valor for **maior que 9**, o dígito é **0**; caso contrário, é o próprio valor.

###  Segundo dígito

1. Multiplicar os **9 primeiros dígitos + o primeiro dígito calculado** por uma sequência de **11 a 2**.
2. Repetir os mesmos passos da lógica acima.

---

## ⚠️ Observações importantes

- **CPFs com todos os dígitos iguais** (ex: `111.111.111-11`) são considerados inválidos, mesmo que passem no cálculo dos dígitos verificadores.
- Este projeto considera apenas a **lógica matemática**, não valida formatação com pontos e hífens.

---

## 💻 Exemplo de uso

```python
from validador import ValidaCPF

cpf = ValidaCPF("123.456.789-09")
if cpf.eh_valido():
    print("CPF válido!")
else:
    print("CPF inválido!")
```

## ▶️ Como rodar via terminal

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/validador-cpf.git
cd ValidadorDeCPF
```

2. Execute o Validador(ou algum dos testbench presentes no arquivo):
```bash
python tb1.py
```

## 🎯 Objetivo do projeto

Este microprojeto foi desenvolvido com o intuito de:

- Consolidar conhecimentos em **Orientação a Objetos (OO)** em Python.
- Praticar conceitos como **classes**, **encapsulamento** e **responsabilidade única**.
- Criar uma base sólida para projetos mais complexos no futuro.
