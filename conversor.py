def celsius_to_fahr(temp):
    return ((temp*9/5)+32)

def fahr_to_celsius(temp):
    return ((temp-32)*(5/9))

def celsius_to_kelv(temp):
    return (temp + 273)


def kelv_to_celsius(temp):
    return (temp - 273)


def kelv_to_fahr(temp):
    return ((temp-273)*(9/5)+32)


def fahr_to_kelv(temp):
    return ((temp-32)*(5/9)+273)

def main():
    print("---Conversor de temperatura----")
    print("Escolha a opção de conversão:")
    print("1: Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Kelvin para Fahrenheit")
    print("6. Fahrenheit para Kelvin")
    print("7. Sair")

    while True:
        choice = input("\nDigite sua escolha: 1, 2, 3, 4, 5, 6 ou 7: ")

        if choice == '7':
            print("Saindo do conversor")
            break
        if choice in ['1', '2', '3', '4', '5', '6']:
            try: 
                temp = float(input("Digite a temperatura desejada: "))

                if choice == '1':
                    converted_temp = celsius_to_fahr(temp)
                    print(f"{temp}ºC é igual {converted_temp: .2f}ºF")
                elif choice == '2': 
                    converted_temp = fahr_to_celsius(temp)
                    print(f"{temp}ºF é igual {converted_temp: .2f}ºC")
                elif choice == '3':
                    converted_temp = celsius_to_kelv(temp)
                    print(f'{temp}ºC é igual {converted_temp}ºK')
                elif choice == '4':
                    converted_temp = kelv_to_celsius(temp)
                    print(f'{temp}K é igual {converted_temp}ºC')
                elif choice == '5':
                    converted_temp = kelv_to_fahr(temp)
                    print(f'{temp}K é igual {converted_temp}F')
                elif choice == '6':
                    converted_temp = fahr_to_kelv(temp)                   
                    print(f'{temp}F é igual {converted_temp}K')
            except ValueError:
                print("Entrada inválida. Por favor, digite algum número para a temperatura")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
    else:
        print("Opção inválida! Por favor, selecione uma das três opções: 1, 2 ou 3")


if __name__ == "__main__":
    main()


