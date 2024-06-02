words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESUTDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
for word in words:
    print(f'\nNa palavra {word} temos', end=' ')
    for leter in word:
        if leter in 'AEIOU':
            print(leter.lower(), end=' ')
