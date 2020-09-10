class Pessoa:
  olhos = 2

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
valdo.olhos = 3
print(valdo.__dict__)
print(kelvin.__dict__)
print(id(valdo.olhos), id(kelvin.olhos), id(Pessoa.olhos))
print(valdo.olhos)
print(kelvin.olhos)
del valdo.olhos
print(valdo.__dict__)
