from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(6) # LZ: changed 5 to 6 -> ska flytta ned
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
        runner = cls() # LZ - only need to initiate one time
        no = False
        
        while True:
            # runner.dice = Die.create_dice(6)

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
                c = 0 # LZ reset lose-counter
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c += 1 # LZ 
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.rounds += 1

            if c > 5 and guess == runner.answer(): 
            # LZ: if loses more than 5 times _in a row_, not 5 times in total
            # also added that the answer has to be correct with ==
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                # break # LZ, no need to break, go to y/n instead

            while True: # LZ: added this while-loop, fixed input == n, and otherwise ask again
                prompt = input("Would you like to play again?[Y/n]: ")
                if prompt == 'y' or prompt == '':
                    break
                elif prompt == 'n':
                    no = True
                    break
                else:
                    print('I did not understand that. Would you like to play again?[Y/n]: ')
                    continue
            
            if no == True:
                break
                
            runner.dice = Die.create_dice(6) # set up new round in end
