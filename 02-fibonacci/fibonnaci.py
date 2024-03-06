def is_fibonacci(number):
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number

def main():
    number = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
