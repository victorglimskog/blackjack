'''
Hand keeps track of cards on hand and total value of them
'''
class Hand():

    def __init__(self, initial_cards = []):
        self.cards = initial_cards

    def __str__(self):
        return f'{self.cards}'

    def get_card_info(self,hidden_cards = 0):
        card_list = self.cards
        for i in range(hidden_cards):
            card_list[i] = '?'
        return card_list