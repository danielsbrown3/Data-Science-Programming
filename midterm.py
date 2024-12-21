def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    
    # write code here and update return statement with your dictionary

    # declare dictionary
    retweetDict = {}
    # loop through each line (element of tweets)
    for line in tweet_list:
        # if RT then select @ to : store in dictionary 
        if 'RT' in line:
            tweetLine = line.split()
            for word in tweetLine:
                if "@" in word:
                    #if the key is already in the dictionary add 1 to the value
                    if str(word[1:-1]) in retweetDict:
                        retweetDict[str(word[1:-1])] += 1
                    #else start a new key balue pair with the key
                    else:
                        retweetDict[str(word[1:-1])] = 1  
    return (retweetDict)

def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    #size requirments for specific grid
    sizeGridrow = range(top,bottom)
    sizeGridcolumn = range(left,right)
    #declare storeGrid list
    storeGrid =[]
    
    #loop through each of grid 
    for row in sizeGridrow:
        rowString = ''
        #loops through each column checking if the coordinates match any of the two coordinates in each tuples in deposits
        for column in sizeGridcolumn:
            #if it matches then concatenate an x
            if any((row,column) == deposit[:2] for deposit in deposits):
                rowString = rowString + 'x'
            #else concatenate a -
            else:
                rowString = rowString + '-'
                
        storeGrid.append(rowString)
    
    return '\n'.join(storeGrid)
        
def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    # Do not alter the function header.  
    # Just fill in the code so it returns the correct number of tons.
    totalSum = 0
    #check each coordinate in the deposits if the first two coordinates are in range then add the third tons value of that tuple
    for deposit in deposits:
        if deposit[0] >= top and deposit[0] < bottom and deposit[1] >= left and deposit[1] < right:
            totalSum += deposit[2]
        
    
    return totalSum

def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    count = 0
    # Store each date in a dictionary so that we can attach a value pair
    dateDict = {}
    for date in dates_list:
        # if its not in the dictionary add it to the dictionary
        if date not in dateDict:
            dateDict[date] = 1
        else:
            #if it is in the dictionary add the current amount of pairs stored in the value of the 
            #dictionary and then add one for the current additional pair
            count += dateDict[date]
            dateDict[date] += 1
            
    return count      
