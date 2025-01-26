def is_in_fibonacci(number):
    # Inicializando a sequência
    a, b = 0, 1
    fibonacci_sequence = [a, b]

    # Gerando a sequência até ultrapassar o número
    while b < number:
        a, b = b, a + b
        fibonacci_sequence.append(b)

    # Verifica se o número está na sequência
    if number in fibonacci_sequence:
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} NÃO pertence à sequência de Fibonacci.")

# Teste
number = int(input("Informe um número para verificar: "))
is_in_fibonacci(number)
