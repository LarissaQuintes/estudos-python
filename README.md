# Estudos de Python 🐍

Repositório com os exercícios que faço enquanto estudo Python, organizados por assunto.

## 📌 Objetivo

Praticar o que aprendi no curso da Alura **Praticando Python: condicionais if, elif e else**, resolvendo problemas de lógica. Em alguns exercícios, fui além do que foi pedido, acrescentando validação de entrada e tratamento de erros.

## 📂 Conteúdo

- `condicionais`: 10 exercícios com estruturas condicionais, como cálculo de IMC, controle de orçamento e aprovação de empréstimo.

## ✅ O que pratiquei

- [x] `if`, `elif` e `else`
- [x] Operadores de comparação e operadores lógicos (`and`, `or`)
- [x] Validação de intervalos
- [x] Validação de entrada com `while True` e `try`/`except`

## 💡 O que aprendi na prática

- Em `and` e `or`, cada lado precisa ser uma comparação completa: `a > 0 and b > 0`, e não `a and b > 0`.
- Intervalo "dentro" se escreve como numa reta: `0 <= nota <= 10`. Intervalo "fora" usa `or`.
- Validar a entrada antes de calcular evita resultados errados e erros no programa.
- Para aceitar números com vírgula, troco por ponto antes de converter: `float(entrada.replace(",", "."))`.
- Zero é par: `0 % 2 == 0`.

## ▶️ Como executar

Clone o repositório:

``` bash
git clone https://github.com/LarissaQuintes/estudos-python
```

Entre na pasta e rode o exercício que quiser:

``` bash
cd estudos-python
python condicionais/nome_do_exercicio.py
```

## 🛠️ Tecnologias

- Python 3
