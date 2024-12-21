def score_word(valid_words):
    '''
    This function takes the list of valid scrabble words made from the scrabble rack and computes a score based on the pretermined dictionary "scores".
    '''
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
    #takes the valid_words list and computers the score based on the letters found in the score dictionary above
    total_score = sum(scores[letter.lower()] for letter in valid_words)
    return total_score