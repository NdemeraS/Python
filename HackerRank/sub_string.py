test_str = "BANANA"

# initializing substring 
def minion_game(string):

    players = {"Stuart": 0, "Kevin": 0}

    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"

    for key in players:
        print(key)
        if key == "Stuart":
            # printing original string 
            print("The original string is : " + string) 

            
            #list the vowels or consensents
            list_of_letters = list_of_letter(consonants, string)
            print(list_of_letters)


            #make the lists of substrings
            list_of_words = list_of_word(list_of_letters, string)

            #remove duplicates
            list_of_words = list(set(list_of_words))

            print(list_of_words)                

            ## starting the count
            players[key] = count(list_of_words, string)

            print(players[key])

        else:
            # printing original string 
            print("The original string is : " + string) 

            
            #list the vowels or consensents
            list_of_letters = list_of_letter(vowels, string)
            print(list_of_letters)


            #make the lists of substrings
            list_of_words = list_of_word(list_of_letters, string)

            #remove duplicates
            list_of_words = list(set(list_of_words))

            print(list_of_words)
                

            ## starting the count
            players[key] = count(list_of_words, string)

            print(players[key])

    #Who one

    if players["Stuart"] > players["Kevin"]:
        print("Stuart " + str(players["Stuart"]))
    else:
        print("Kevin " + str(players["Kevin"]))
    


def list_of_letter(check_str, string):
        list_of_letter = []

        for item in check_str:

            if item in string:
                list_of_letter.append(item)

        return list_of_letter


def list_of_word(list_of_letters, string):

    list_of_words = []

     # conuter for tracking const/vowels within test_str
    cons_ind = 0

    for item in list_of_letters:

        #counter for spilicing the main string
        x = 0



        while x < len(string) + 1:

            if item == string[cons_ind]:

                splice = item + string[cons_ind + 1:x]
                # print(splice)
                list_of_words.append(splice)
            else:
                cons_ind = cons_ind + 1


            x = x + 1

    return list_of_words



def  count (list_of_words, string):

    sum = 0
    for test_sub in list_of_words:

        
        #lists of words constructs to check how many times they occurt
        res = [i for i in range(len(string)) if string.startswith(test_sub, i)] 
        print(str(test_sub) + " " +  str(len(res)))

        sum = sum + len(res)
    
    return sum
        

minion_game(test_str)

