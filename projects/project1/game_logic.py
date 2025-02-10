from typing import Iterable, Optional
from datastructures.ibag import IBag, T
from datastructures.bag import Bag
from projects.project1.cards import Card, MultiDeck
import random
from copy import deepcopy



class Game:
    
    def __init__(self) -> None:
        self.deck = MultiDeck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        print("-----------------------")
        print("Welcome to Blackjack!")
        print("")

    def play(self):

        def calculate_score(hand):
            score = 0
            for card in hand:
                if card.value == 'A':
                    score += 11
                elif card.value in ['J', 'Q', 'K']:
                    score += 10
                else:
                    score += int(card.value)
            
            if score > 21 and 'A' in [card.value for card in hand]:
                score -= 10     # implementing the A = 1 or 11
            return score

        
        def show_hand(hand, person):
            print(f"{person} Hand:", end = " ")
            for i in range(len(hand)):
                print(f"[{hand[i].symbol}]", end = " ")
            print(f"| Score: {calculate_score(hand)}")
    

        def init_deal():
            for i in range(2):
                self.player_hand.append(self.deck.draw_random_card())
            for i in range(2):
                self.dealer_hand.append(self.deck.draw_random_card())

            print("Initial Deal:")
            show_hand(self.player_hand, "Player")
            print(f"Dealer Hand: [{self.dealer_hand[0].symbol}] [Hidden] | Score: {calculate_score([self.dealer_hand[0]])}")
                # only calculates score based on dealer's first card
            print("")

            if calculate_score(self.dealer_hand) == 21:     # WIN CASE
                print("")
                show_hand(self.dealer_hand, "Dealer")
                print("Dealer has Blackjack! Dealer wins! Better luck next time.")
                self.game_over = True
            elif calculate_score(self.player_hand) == 21:   # WIN CASE
                print("")
                print("\u265b Player has Blackjack! Player wins!")
                self.game_over = True


        def player_choice():
            choice = input("Would you like to (H)it or (S)tay? ")

            if choice not in ['H', 'S']:
                print("Sorry, I don't understand that choice. Your options are H (Hit) or S (Stay).")
                print("")
                player_choice()

            elif choice == 'H':     # hit case
                self.player_hand.append(self.deck.draw_random_card())
                show_hand(self.player_hand, "Player")
                
                if calculate_score(self.player_hand) > 21:      # WIN CASE
                    print("Bust! You went over 21.")
                    print("")
                    print("Dealer wins! Better luck next time!")
                    self.game_over = True
                else:
                    print("")
                    player_choice()

            elif choice == 'S':     # stay case (just for documentation)
                print("")


        def dealer_reveal():
            ''' Dealer reveals hand, draws until reaching 17 '''
            show_hand(self.dealer_hand, "Dealer")
            
            while calculate_score(self.dealer_hand) < 17:
                print("Dealer draws.")
                self.dealer_hand.append(self.deck.draw_random_card())
                show_hand(self.dealer_hand, "Dealer")
                
                if calculate_score(self.dealer_hand) > 21:      # WIN CASE
                    print("")
                    print("\u265b Player wins! Dealer busted.")
                    self.game_over = True
            print("")


        def final_score():
            ''' Final scores are displayed and the one with a score closest to 21 wins. '''
            print("Final hands:")
            show_hand(self.player_hand, "Player")
            show_hand(self.dealer_hand, "Dealer")
            print("")

            # WIN CASES
            if calculate_score(self.player_hand) > calculate_score(self.dealer_hand):
                print("\u265b Player wins!")
            elif calculate_score(self.dealer_hand) > calculate_score(self.player_hand):
                print("Dealer wins! Better luck next time.")
            elif calculate_score(self.dealer_hand) == calculate_score(self.player_hand):
                print("It's a tie!")
            
            print("")
            self.game_over = True

        
        def replay_choice():
            print("")
            replay = input("Would you like to play again? (Y)es or (N)o: ")

            if replay not in ['Y', 'N']:
                print("Sorry, I don't understand that choice. Your options are Y (Replay) or N (Quit).")
                print("")
                replay_choice()
            elif replay == 'Y':     # replay case
                print("")
                blackjack = Game()
                blackjack.play()
            elif replay == 'N':     # quit case
                print("Game over! Thanks for playing!")
                print("")
                # will reach end of program



        while not self.game_over:
            init_deal()
            if not self.game_over:
                player_choice()
            if not self.game_over:
                dealer_reveal()
            if not self.game_over:
                final_score()
        replay_choice()
    


        
            
