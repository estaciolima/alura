class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano

    def dar_like(self):
        self._likes += 1

    

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return(f'Nome: {self.nome}\nAno: {self._ano}\nDuracao: {self.duracao} min\nLikes: {self.likes}\n')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return(f'Nome: {self.nome}\nAno: {self._ano}\nTemporadas: {self.temporadas}\nLikes: {self.likes}\n')


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    def __len__(self):
        return len(self._programas)

vingadores = Filme("Vingadores guerra infinita", 2010, 120)
vingadores.dar_like()
vingadores.dar_like()
sexeducation = Serie("Sex Education", 2018, 4)
rei_leao = Filme("Rei Leao", 1999, 120)
madagascar = Filme("Madagascar", 2010, 110)
breaking_bad = Serie("Breaking Bad", 2001, 8)
programas = [vingadores, sexeducation,
            rei_leao, madagascar, breaking_bad]

playlist = Playlist("filmes favoritos", programas)

print(f"Tamanho da playlist que eu criei: {len(playlist)}")

for programa in playlist:
    print(programa)