#Miniteste feito por: Vinícius Gonçalves de Oliveira e Vitor Melo da Silva

class SenhaInvalida(Exception):
  pass

class PilhaArray:

  def __init__(self):
    self.senha = []
    self.maiusculo = []
    self.minusculo = []
      
  def __len__(self):
    return len(self.senha)

  def push(self, e):
    self.senha.append(e)

  def valida_senha(self, i = 0):
    if len(self.senha) == i:    
      if len(self.maiusculo) != len(self.minusculo) or len(self.senha) == 0:
        raise SenhaInvalida('senha inválida')
      else: 
        return 'Senha válida'
    elif self.senha[i] == self.senha[i].upper():
      self.maiusculo.append(self.senha[i])
      return self.valida_senha(i+1)
    elif self.senha[i] == self.senha[i].lower():
      if self.senha[i].upper() == self.maiusculo[-1]:
        self.minusculo.append(self.senha[i])
        self.maiusculo.pop(-1)
        self.minusculo.pop(-1)
        return self.valida_senha(i+1)
      else:
        raise SenhaInvalida('senha INVALIDA')        
              
if __name__ == '__main__':
  try:
    s = PilhaArray()
    s.push('A')
    s.push('B')
    s.push('C')
    s.push('c')
    s.push('D')
    s.push('E')
    s.push('e')
    s.push('d')
    s.push('b')
    s.push('a')
    print(s.valida_senha())
  except:
    print('Senha inválida')
    
    
# ['A', 'B', 'C', 'D', 'E']
# ['c', 'e', 'd', 'b', 'a']
