def celsius_to_fahr(temp):
    return ((temp*9/5)+32)

def fahr_to_celsius(temp):
    return ((temp-32)*(5/9))

def main():
    print("---Conversor de temperatura----")
    print("Escolha a opção de conversão:")
    print("1: Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")

    while True:
        choice = input("\nDigite sua escolha: 1, 2 ou 3: ")

        if choice == '3':
            print("Saindo do conversor")
            break
        if choice in ['1', '2']:
            try: 
                temp = float(input("Digite a temperatura desejada: "))

                if choice == '1':
                    converted_temp = celsius_to_fahr(temp)
                    print(f"{temp}ºC é igual {converted_temp: .2f}ºF")
                else: 
                    coverted_temp = fahr_to_celsius(temp)
                    print(f"{temp}ºF é igual {converted_temp: .2f}ºC")
                    
            except ValueError:
                print("Entrada inválida. Por favor, digite algum número para a temperatura")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
    else:
        print("Opção inválida! Por favor, selecione uma das três opções: 1, 2 ou 3")


if __name__ == "__main__":
    main()


