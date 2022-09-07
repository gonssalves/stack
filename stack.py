class PilhaVazia(Exception):
    pass

class SenhaInvalida(Exception):
    pass

class PilhaArray:

    def __init__(self):
        self._items = []
        self.senha = []
        self.maiusculo = []
        self.minusculo = []
        
    def __len__(self):
        return len(self._items)

    def size(self):
        return self.__len__()

    def is_empty(self):
        return len(self._items) == 0

    def push(self, e):
        self._items.append(e)

    def top(self):
        if self.is_empty():
            raise PilhaVazia('pilha vazia')
        return self._items[-1]

    def pop(self):
        if self.is_empty():
            raise PilhaVazia('pilha vazia')
        return self._items.pop()

    def valida_senha(self, i=0):
        if len(self._items) == i:    
            if len (self.maiusculo) == 0 or len(self.minusculo) == 0 or len(self.maiusculo) != len(self.minusculo):
                raise SenhaInvalida('senha inválida')
            else:
                self.count = 0
                for j,k in zip(self.maiusculo, self.minusculo):
                    if j.lower() == k:
                        self.count +=1  
            return 'Senha válida'
        elif self._items[i] == self._items[i].upper():
            self.maiusculo.append(self._items[i])
            return self.valida_senha(i+1)
        elif self._items[i] == self._items[i].lower():
            self.minusculo.append(self._items[i])
            return self.valida_senha(i+1)
        
              
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
