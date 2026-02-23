# Aula 9 – Manipulando Texto (VERSÃO COMPLETA)
print()
texto = input('Digite seu nome completo: ')

print('\n🔎 ===== ANÁLISE =====')

print(f'O nome possui {len(texto)} caracteres.')
print(f'Os primeiros 10 caracteres são: {texto[0:10]}')
print(f'A letra "a" aparece {texto.count("a")} vezes.')
print(f'A primeira letra "o" está na posição: {texto.find("o")}')
print(f'A última letra "a" está na posição: {texto.rfind("a")}')
print(f'Começa com "Ale"? {texto.startswith("Ale")}')
print(f'Termina com "gomes"? {texto.endswith("gomes")}')
print(f'Só tem letras? {texto.isalpha()}')
print(f'É alfanumérico? {texto.isalnum()}')
print(f'Só tem espaços? {texto.isspace()}')
print(f'Quantas letras tem o primeiro nome: {texto.find(' ')} letras ')

print('\n🔄 ===== TRANSFORMAÇÕES =====')

print(f'Trocando "Lucas" por "Santiago": {texto.replace("Lucas", "Santiago")}')
print(f'MAIÚSCULO: {texto.upper()}')
print(f'Minúsculo: {texto.lower()}')
print(f'Title (iniciais maiúsculas): {texto.title()}')
print(f'Invertendo maiúsc/minúsc: {texto.swapcase()}')
print(f'Centralizado com "-": {texto.center(40, "-")}')

print('\n✂ ===== REMOÇÃO DE ESPAÇOS =====')

print(f'Strip (remove início e fim): "{texto.strip()}"')
print(f'LStrip (remove esquerda): "{texto.lstrip()}"')
print(f'RStrip (remove direita): "{texto.rstrip()}"')

print('\n🔀 ===== DIVISÃO =====')

print(f'Split (transforma em lista): {texto.split()}')
print(f'Partition (divide na primeira ocorrência de espaço): {texto.partition(" ")}')
print(f'RPartition (divide da direita): {texto.rpartition(" ")}')

print('\n🆕 ===== PREFIXO / SUFIXO =====')

print(f'Removendo prefixo "Alessandra": {texto.removeprefix("Alessandra")}')
print(f'Removendo sufixo "gomes": {texto.removesuffix("gomes")}')

print('\n🔢 ===== EXEMPLO COM NÚMEROS =====')

numero = "123"
print(f'Número com zeros à esquerda (zfill): {numero.zfill(6)}')