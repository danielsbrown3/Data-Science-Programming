import random

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        #generates a random float between 0 and  1
        self.__probability = random.uniform(0, 1)

    def __repr__(self):
        '''User object with secret probability'''
        #returns the random click probability to three decimal places
        return f'Click Probability: {self.__probability:.3f}'

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        #returns the random click probability to three decimal places
        return f'Click Probability: {self.__probability:.3f}'

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise, based on secret probability.'''
        #if probability is greater than random number return true else false
        return random.random() < self.__probability

class Auction:
    '''Class to represent an online second-price ad auction'''
    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        #Initialize users and bidders from inputs
        self.users = users
        self.bidders = bidders
        #Initialize balances as dictionary that is gonna store the bidders and their balance
        self.balances = {}
        #Set each bidders initial bid to 0
        for bidder in bidders:
            self.balances[bidder] = 0

    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        #returns users and qualified bidders using f string
        return f'Auction Users: {len(self.users)} Auction Bidders: {len(self.bidders)}'

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return f'Auction Users: {len(self.users)} Auction Bidders: {len(self.bidders)}'

    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price'''
        #randomly picks a user from the list of users
        user = random.choice(self.users)

        #Intialize bids as a dictionary
        bids = {}
        #loops through each bidder and calls the bid method to get their bid
        #then assigns the bid amount ot that user in the bids dictionary
        for bidder in self.bidders:
            if self.balances[bidder] >= -1000:
                bid_amount = bidder.bid(user)
                bids[bidder] = bid_amount

        if not bids:
            return

        #assigns the winner as the user with the maximum bid value
        winner = max(bids, key=bids.get)

        #create winning bid object from the value of the winner key
        winning_bid = bids[winner]


        second_highest_bid = 0
        #find second highest bidder if more than one bid
        if len(bids) > 1:
            #take the max bid out by checking if bid is max bad and if its is removing it
            bids_minus_max = [bid for bid in bids.values() if bid != winning_bid]
            #finds the max of the new list making the value the second highest value
            second_highest_bid = max(bids_minus_max)
        else:
            #if there is just 1 bid then that is the second and highest bid
            second_highest_bid = winning_bid



        #inilitialize user clicked object that stores true or false depending on if the user clicked
        user_clicked = user.show_ad()

        #loops through each bidder to update balance and notify
        for bidder in self.bidders:

            #check if the current bidder is the winner
            auction_winner = bidder == winner

            if auction_winner:
                #if bidder won then subtract the second highest bid (actual price)
                self.balances[bidder] -= second_highest_bid

                if user_clicked:
                    #if the user clicked the add then add 1 to the winning bidder's balance
                    self.balances[bidder] += 1

                #notify winning bidder of price, user outcome, and updated balance
                bidder.notify(True, second_highest_bid, user_clicked)
            else:
                #notify losing bidders of price
                bidder.notify(False, second_highest_bid, None)
