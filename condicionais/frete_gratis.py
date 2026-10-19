valor_da_compra = float(input("\nDigite o valor da compra: ").replace(",", "."))
cep = input("Digite o número do CEP: ")


if valor_da_compra <= 0:
    print("\nValor da compra é inválido.")
elif len(cep) != 8:
    print("\nA quantidade de números no CEP é inválida.")
else:
    if valor_da_compra > 200 and cep.startswith("2"):
        valor_final = valor_da_compra
        print("\nfrete grátis.")
    else:
        valor_final = valor_da_compra + 15
        print("\nFrete R$15,00.")

    print(f"Valor final: R${valor_final:.2f}")