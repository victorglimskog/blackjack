from deck import Deck
from bankroll import Bankroll
from hand import Hand

def print_game_screen(bankroll, bet, player_hand, dealer_hand):
    '''
    Print the current state of game to view
    '''
    print('\n================')
    print(f'\nBet: ${bet}\nBankroll: ${bankroll}')
    print('------------------')
    print(f'Player cards: {player_hand.get_card_info()}')
    print(f'Dealer cards: {dealer_hand.get_card_info(1)}')

def next_bet(bankroll):
    while True:
        try:
            bet_request = int(input(f'Your current balance is ${bankroll}, how much do you want to bet?\n'))
        except:
            print('Thats is not a number')
            continue
        else:
            bet = bankroll.withdraw(bet_request)
            if bet < 1:
                print('Too poor, try again: ')
                continue
            else:
                return bet

def draw_cards(deck, number):
    cards = []
    for i in range(number):
        cards.append(deck.next_card())
    return cards

def game():
    '''
    Main game loop
    '''

    input('Welcome to Black Jack. Press any key to play')
    deck = Deck()
    bankroll = Bankroll(100)
    play = True

    # One round of the game loop
    while play == True:
        bet = next_bet(bankroll)
        player_hand = Hand(draw_cards(deck, 2))
        dealer_hand = Hand(draw_cards(deck, 2))
        print_game_screen(bankroll, bet, player_hand, dealer_hand)
        play = False

if __name__ == '__main__':
    game()