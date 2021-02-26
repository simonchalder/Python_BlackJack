from random import choice as rc
import random
from time import sleep

class Player:
    def __init__(self):
        self.deck = (1,2,3,4,5,6,7,8,9,10)
        self.suits = ('H','D','C','S')
        self.hand = []
        self.name = ''
        self.pot = 100
        self.bet = 0

    
    def add_card(self):
       self.hand.append(rc(self.deck))
       return self.hand
       
    
    def total_score(self):
        self.player_score = sum(self.hand)
        if 1 in self.hand and self.player_score <= 21:
            self.player_score += 10
        else:
            self.player_score = self.player_score
        if self.player_score > 21:
            print('BUST!!! Dealer Wins.')
            print('------------------')
            print()
            print(f'Player Hand: {self.hand}')
            print()
            print(f'Player Score: {self.player_score}')
            self.hand = []
            d1.hand = []
            self.player_score = 0
            d1.dealer_score = 0
        else:
            print('------------------')
            print()
            print(f'Player Hand: {self.hand}')
            print()
            print(f'Player Score: {self.player_score}')

    def gamble(self):
        print(f'Chips Available: {self.pot}')
        self.bet = input('Place Bet: ')
        self.bet = int(self.bet)
        self.pot -= self.bet
        print()
        print(f'Bet Placed: {self.bet}')
        return self.bet

    def game(self):
        self.action = ''
        while self.action.lower() != 'q':
            self.action = input('''
------------------
Type "S" to HOLD
Type "H" to HIT
Type "Q" to QUIT
>   ''')
            if self.action.lower() == 'h':
                self.add_card()
                self.total_score()
            elif self.action.lower() == 's':
                print(f'Final Score: ')
                self.total_score()
                break
            elif self.action.lower() == 'q':
                print('Thankyou for playing.')
                quit()


class Dealer:
    def __init__(self):
        self.deck = (1,2,3,4,5,6,7,8,9,10)
        self.suits = ('H','D','C','S')
        self.hand = []
        self.name = ''
        self.is_bust = False

    # DEALER
    def add_card(self):
        self.hand.append(rc(self.deck))
        print(self.hand) 
        return self.hand
        

    # DEALER
    def game(self):
        self.dealer_score = sum(self.hand)
        print(f'Dealer Score: {self.dealer_score}')
        while self.dealer_score < 30 and self.dealer_score < p1.player_score:                
            if self.dealer_score >= 22:
                self.is_bust = True
                print(f'BUST!!! on {self.dealer_score}')
            elif self.dealer_score < 16:
                self.add_card()
                self.dealer_score = sum(self.hand)
                print(f'Dealer Score: {self.dealer_score}')
                print()
                sleep(3)
                continue
            elif self.dealer_score >= 16 and self.dealer_score < 18:
                self.hit_chance = round(random.random(), 2)
                if self.hit_chance <= 0.10:
                    self.add_card()
                    self.dealer_score = sum(self.hand)
                    print(f'Dealer Score: {self.dealer_score}')
                    print()
                    sleep(3)
                    continue
                else:
                    print(f'Dealer Holds on {self.dealer_score}')
                    print()
                    sleep(3)
                    return self.dealer_score
            elif self.dealer_score >= 18 and self.dealer_score < 21:
                self.hit_chance = round(random.random(), 2)
                if self.hit_chance <= 0.10:
                    self.add_card()
                    self.dealer_score = sum(self.hand)
                    print(f'Dealer Score: {self.dealer_score}')
                    print()
                    sleep(3)
                    continue
            elif self.dealer_score == 21:
                print(f'Dealer Holds on {self.dealer_score}')
                sleep(3)
                return self.dealer_score
            else:
                print(f'Dealer Holds on {self.dealer_score}')
                sleep(3)
                return self.dealer_score
        


    def check_blackjack(self):
        self.dealer_score = sum(self.hand)
        if self.dealer_score == 21:
            print('Blackjack Dealer Wins!!!')
            quit()
        else:
            print('Dealer does not have Blackjack')


def main():
    p1.gamble()
    p1.add_card()
    p1.add_card()
    p1.total_score()
    p1.game()
    d1.add_card()
    d1.add_card()
    d1.check_blackjack()
    d1.game()
    winner()
    main()

def winner():
    print(f'Player Score: {p1.player_score}')
    print()
    print(f'Dealer Score: {d1.dealer_score}')
    print()
    print(20 * '*')
    if p1.player_score > d1.dealer_score or d1.is_bust == True:
        print('Congratulations Player Wins!')
        p1.pot += round(p1.bet * 1.5)
        print(f'Player Wins: {round(p1.bet * 1.5)}')
        p1.hand = []
        d1.hand = []
        p1.player_score = 0
        d1.dealer_score = 0
    elif p1.player_score == d1.dealer_score:
        print('Game is Tied')
        print('All Bets Returned')
        p1.pot += p1.bet
        p1.hand = []
        d1.hand = []
        p1.player_score = 0
        d1.dealer_score = 0
    else:
        print('Dealer Wins. Better luck next time')
        p1.hand = []
        d1.hand = []
        p1.player_score = 0
        d1.dealer_score = 0

p1 = Player()
d1 = Dealer()
main()