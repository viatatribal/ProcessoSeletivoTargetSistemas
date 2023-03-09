# 5) Escreva um programa que inverta os caracteres de um string. 
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de 
# sua preferência ou pode ser previamente definida no código; 
# b) Evite usar funções prontas, como, por exemplo, reverse; 


def revstring(str):
    size = len(str)
    revstr = ""
    while size > 0:
        revstr += str[size-1]
        size -= 1
    return revstr

# Basta chamar a função com a string que deseja inverter:
print(f'{revstring("job")}')      # "boj"
print(f'{revstring("rotation")}') # "rotation"
print(f'{revstring("ribeirao")}') # "oariebir"
