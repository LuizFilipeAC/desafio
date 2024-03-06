def fibonacci(indice):
    return indice[0] + indice[1]

def adding_removing(x):
    fibonacci_start.append(next_number)
    fibonacci_sequence.append(next_number)
    fibonacci_start.pop(0)
    
def checking_number(number):
    try:
        number = int(number)
    except ValueError:
        return False
    
    
fibonacci_start = [0, 1]
fibonacci_sequence = [0, 1]

check = True

while check:
    value = input(
    'Insira um número e descubra se ele pertence a sequência de Fibonacci!!\n'
    'Verifique um valor -> ')
    checking = checking_number(value)

    if checking is False: # em caso da checagem retornar verdadeiro
        print('Você inseriu um dado não numérico, por favor, faça novamente!')
        continue
    else:
        check = False
    
    
    
while True:
    next_number = fibonacci(fibonacci_start)
    adding_removing(next_number)
    if fibonacci_sequence[-1] >= int(value):
        break
 
   
if int(value) in fibonacci_sequence:
    print(f'O número {value} pertence a sequência Fibonacci!')
else:
    print(f'O número {value} não pertence a sequência Fibonacci')
    
print(
    '\n'
    'sequência Fibonacci\n'
    f'{fibonacci_sequence}...')