class Pessoa:
  def __init__(self, *filhos, nome=None, idade=29):
    self.nome = nome
    self.idade = idade
    self.filhos = list(filhos)

  def cumprimentar(self):
    return f'Ola {id(self)}'

if __name__=='__main__':
  kelvin = Pessoa(nome='kelvin')
  valdo = Pessoa(kelvin, nome='valdo')
  print(Pessoa.cumprimentar(valdo))
  print(id(valdo))
  print(valdo.cumprimentar())
  print(valdo.nome)
  print(valdo.idade)
  for filho in valdo.filhos:
    print(filho.nome)
valdo.sobrenome = 'Torres'
del valdo.filhos
print(valdo.__dict__)
print(kelvin.__dict__)
