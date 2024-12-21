
import sys
from wordscore import score_word

def run_scrabble(scrabbleRack):
    
    '''
    This function takes scrabble rack as an input and will return each word that can be formed from the letters within the rack.
    
    This is done by looping over every word in the scrabble word database and testing if each letter is found in the scrabble rack.
    
    The function wordscore returns the score of each found scrabble word from a predefined scorelist for each letter.
    '''
    #if the function argument is not between 2 to 7 characters return error
    if len(scrabbleRack) > 7 or len(scrabbleRack) < 2:
        return "Please enter a two to seven letter word for your scrabble rack."
    
    if not all(character.isalpha() or character in ['*','?'] for character in scrabbleRack):
        return "Please use letters A-Z or * and ?"

    if scrabbleRack.count('*') > 1 or scrabbleRack.count('?') > 1:
        return "Error please only use 1 wildcard"

    #reading the data
    try:
        with open("sowpods.txt","r") as infile:
            raw_input = infile.readlines()
            data = [datum.strip('\n') for datum in raw_input]
    except:
        return "Error file not found."
    
    
    #initialize the words list
    valid_words = []
    #set all scrabble rack letters to uppercase
    scrabbleRack = scrabbleRack.upper()
    
    
    #search through each word of scrabble list
    for word in data:
        #creates storing variable for the scrabble rack as a list so that it becomes mutable
        tempRack = list(scrabbleRack)
        
        #Assumes the rack letter is found in the scrabble word
        isFoundinData = True
        
        #search through each letter of the current word on the scrabble list
        for letter in word:
            #remove the letter is in the rack remove it with the goal of removing each letter to prove that the word is found in the scrabble list
            if letter in tempRack:
                tempRack.remove(letter)
            
            #wildcard
            elif '*' in tempRack:
                tempRack.remove('*')
                
            #wildcard
            elif '?' in tempRack:
                tempRack.remove('?')
            
            #if neither the letter of the scrabble word, nor *, or ? are found in the rack word than move onto the next scrabble word in the database
            else:
                isFoundinData = False
                break
        #if all letters are successfully removed then append it to the valid_words list
        if isFoundinData:
            valid_words.append((score_word(word),word))
    
    #sorts the list
    valid_words.sort(key=lambda x: (-x[0], x[1]))
    
    return valid_words,len(valid_words)

