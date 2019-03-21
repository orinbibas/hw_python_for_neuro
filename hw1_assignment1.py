def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    last = ''
    to_print = False
    for i in range(len(word)-4):
        if word[i] == last and word[i+1] == word[i+2] and word[i+3] == word[i+4]:
            to_print = True
        else:
            last=word[i]

    return to_print
  
if __name__ == "__main__":
    trifeca(word)
        

                    

