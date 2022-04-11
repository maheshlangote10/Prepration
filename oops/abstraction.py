from abc import ABC, abstractmethod

class Game(ABC):

    @abstractmethod
    def play(self):
        pass

    def stop(self):
        pass

    def start(self):
        pass

    def pause(self):
        pass


class Chess(Game):

    def move(self):
        print("moving")

    def play(self):
        print("Playing chess")

if __name__ == '__main__':
    obj = Chess()
    obj.move()
    obj.play()
    # tryobj = Game()