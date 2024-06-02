from math import sin, cos, tan, radians
n = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {n} tem o SENO de {sin(radians(n)):.2f}')
print(f'O ângulo de {n} tem o COSSENO de {cos(radians(n)):.2f}')
print(f'O ângulo de {n} tem a TANGENTE de {tan(radians(n)):.2f}')
