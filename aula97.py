
# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path


print ( 'Este módulo se chama' , __name__ )
"""
importar  aula97_m
from  aula97_m  import  soma , variavel_modulo

print ( 'Este módulo se chama' , __nome__ )
# print('Este módulo se chama', __name__)
print ( aula97_m . variavel_modulo )
imprimir ( variavel_modulo )
imprimir ( soma ( 2 , 3 ))
print ( aula97_m.soma ( 2,3 ) ) _ _ _



print ( 'Este módulo se chama' , __nome__ )
variavel_modulo  =  'Luiz'


def  soma ( x , y ):
    retornar  x  +  y

"""    