import random

class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''

    def __init__(self, num_users, num_rounds):
        '''Setting initial balance to 0, number of users, number of rounds, and round counter'''
        self.balance = 0
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.round_counter = 0

    def __repr__(self):
        '''Return Bidder object with balance'''
        return f'Bidder Balance: {self.balance}'

    def __str__(self):
        '''Return Bidder object with balance'''
        return f'Bidder Balance: {self.balance}'

    def bid(self, user_id):
        '''Returns a non-negative bid amount'''
        #initilial small bid of 0.1
        base_bid = 0.1
        variation = random.uniform(0, 0.1)
        #adjust bid by the initial bid and a random number from 0 to 0.1
        adjusted_bid = base_bid + variation
        #round balance to 3 digits
        self.balance = round(self.balance,3)

        #if balance large then increase bid
        if self.balance > 10:
            return adjusted_bid + 0.1
        #if we have past more than a quarter of the rounds low bid
        elif self.round_counter > self.num_rounds / 4:
            return max(0.1, adjusted_bid - 0.7)
        else:
        #return normal increased bid
            return adjusted_bid


    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        #if user is disqualified then exit method

        #if notified of auction winner subtract the price of the bid
        if auction_winner:
            self.balance -= price
            #if user clicked add 1 to user balance
            if clicked:
                self.balance += 1

        #round balance to 3 digits
        self.balance = round(self.balance,3)
