from typing import Iterable, Optional
from datastructures.ibag import IBag, T
from datastructures.bag import Bag
from projects.project1.cards import Card, MultiDeck
import random
from copy import deepcopy



class Game:
    
    def __init__(self) -> None:
        ''' Initializes the Blackjack game, including the deck and both hands. '''
        self.deck = MultiDeck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        print("-----------------------")
        print("Welcome to Blackjack!")
        print("")


    def play(self):

        ## USEFUL FUNCTIONS
        
        def calculate_score(hand):
            ''' Calculates the score of a given hand. '''
            
            score = 0
            for card in hand:
                if card.value == 'A':
                    score += 11
                elif card.value in ['J', 'Q', 'K']:
                    score += 10
                else:
                    score += int(card.value)
            
            # implementing the A = 1 or 11 mechanic
            if score > 21 and 'A' in [card.value for card in hand]:
                score -= 10
            return score

        
        def show_hand(hand, person):
            ''' Prints the cards in a given hand and the hand's score to the terminal. '''
            
            print(f"{person} Hand:", end = " ")
            for i in range(len(hand)):
                print(f"[{hand[i].symbol}]", end = " ")     # this way, can print any number of cards
            print(f"| Score: {calculate_score(hand)}")
    

        ## GAME STAGE FUNCTIONS
        
        def init_deal():
            ''' Deals two cards to the dealer and player. Checks for any blackjacks. '''
            
            # deals the cards
            for i in range(2):
                self.player_hand.append(self.deck.draw_random_card())
            for i in range(2):
                self.dealer_hand.append(self.deck.draw_random_card())

            # prints the hands to the terminal
            print("Initial Deal:")
            show_hand(self.player_hand, "Player")
            print(f"Dealer Hand: [{self.dealer_hand[0].symbol}] [Hidden] | Score: {calculate_score([self.dealer_hand[0]])}")
                # only calculates score based on dealer's first card
            print("")

            # checks for blackjacks
            if calculate_score(self.dealer_hand) == 21:     # GAME END
                print("")
                show_hand(self.dealer_hand, "Dealer")
                print("Dealer has Blackjack! Dealer wins! Better luck next time.")
                self.game_over = True
            elif calculate_score(self.player_hand) == 21:   # GAME END
                print("")
                print("\u265b Player has Blackjack! Player wins!")
                self.game_over = True


        def player_choice():
            ''' Player chooses to hit or stay. Depending on choice, may draw a card and print new hand. Checks for bust. '''
            
            # asks for player input
            choice = input("Would you like to (H)it or (S)tay? ")

            # checks for valid input
            if choice not in ['H', 'S']:
                print("Sorry, I don't understand that choice. Your options are H (Hit) or S (Stay).")
                print("")
                player_choice()

            # HIT CASE
            elif choice == 'H':
                # draws a card + prints new hand
                self.player_hand.append(self.deck.draw_random_card())
                show_hand(self.player_hand, "Player")
                
                # checks for bust
                if calculate_score(self.player_hand) > 21:      # GAME END
                    print("Bust! You went over 21.")
                    print("")
                    print("Dealer wins! Better luck next time!")
                    self.game_over = True
                else:
                    print("")
                    player_choice()

            # STAY CASE
            elif choice == 'S':     # (just for documentation)
                print("")


        def dealer_reveal():
            ''' Dealer reveals hand, draws until reaching 17. '''
        
            # reveals dealer hand
            show_hand(self.dealer_hand, "Dealer")
            
            # draws until 17
            while calculate_score(self.dealer_hand) < 17:
                print("Dealer draws.")
                self.dealer_hand.append(self.deck.draw_random_card())
                show_hand(self.dealer_hand, "Dealer")
                
                # checks for bust after each draw
                if calculate_score(self.dealer_hand) > 21:      # END GAME
                    print("")
                    print("\u265b Player wins! Dealer busted.")
                    self.game_over = True
            print("")


        def final_score():
            ''' If no one has busted or has a blackjack, final scores are displayed and the one with a score closest to 21 wins. '''

            # prints final hands and scores
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
            ''' Player is given the choice to quit or replay the game. Restarts game or ends it depending on the choice. '''

            # asks for player input
            print("")
            replay = input("Would you like to play again? (Y)es or (N)o: ")

            # checks for valid input
            if replay not in ['Y', 'N']:
                print("Sorry, I don't understand that choice. Your options are Y (Replay) or N (Quit).")
                print("")
                replay_choice()
            
            # replay case (restarts game)
            elif replay == 'Y':
                print("")
                blackjack = Game()
                blackjack.play()
            
            # quit case (ends program)
            elif replay == 'N':
                print("Game over! Thanks for playing!")
                print("")


        # calls all the game stage functions in order
        while not self.game_over:
            init_deal()
            if not self.game_over:
                player_choice()
            if not self.game_over:
                dealer_reveal()
            if not self.game_over:
                final_score()
        replay_choice()
    


        
            
