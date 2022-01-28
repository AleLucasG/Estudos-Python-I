"""Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome."""

nome = str(input('Digite seu nome: ')).strip()
print('O nome tem “SILVA”: {} \n'.format('SILVA' in nome.upper()))


"""Como Prof. Guanabara fez"""
nome = str(input('Digite seu nome: ')).strip()
print('O nome tem “SILVA”: {}'.format('silva' in nome.lower()))






