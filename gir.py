class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        #ваш код
        self._lives = self._lives - 1
        #print(self._lives)
        if self._lives == 0:
           print("Game Over")

p = Player("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()