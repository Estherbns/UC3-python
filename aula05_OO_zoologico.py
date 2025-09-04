from aula05_class_OO_animal  import Animal   #vai importar a classe Animal do arquivo das classes
from aula05_class_OO_animal  import Cachorro

#ou
# from aula05_class_OO_animal  import *  # - importa todas as classes do arquivo

animal = Animal()  # ele ta herdando do pai
animal.quemSouEu()

cachorro = Cachorro()
cachorro.quemSouEu() 