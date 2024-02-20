from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(6) # LZ: changed 5 to 6
        self.reset()

    def reset(self):
        self.rounds = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value # LZ: fixed total
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        while True:
            runner = cls()

            print("Round {}\n".format(runner.rounds))

            for die in runner.dice:
                print(die.show())

            while True: # LZ - added while-loop and try/except
                guess = input("Sigh. What is your guess?: ")
                try:
                    guess = int(guess)
                    break
                except:
                    print('That was not a number!')
                

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.rounds += 1

            if c > 5:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            else:
                break # LZ 
