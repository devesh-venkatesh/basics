# Function to return user input list
def user_input():

    # initialize list of words
    global words
    words = []

    # For loop to retrieve input values
    for x in range(11):
        if x == 0 or x == 3 or x == 5 or x== 8:
            w = input("adjective: ")
            words.append(w)
        elif x == 1 or x == 6:
            w = input("plural noun: ")
            words.append(w)
        elif x == 2 or x == 10:
            w = input("noun: ")
            words.append(w)
        elif x == 4 or x == 7:
            w = input("body part: ")
            words.append(w)
        else:
            w = input("adverb: ")
            words.append(w)

    # return all the words collected
    return words


# Function to parse words into madlib and print.
def poem_base(data):
    print("The force is a mystical, "+words[0]+" power. As Jedi Master Obi-Wan\n"
          "Kenobi once said, 'The Force is an energy field, created by all living\n"
          + words[1]+", that sourrounds us, penetrates us, and binds the \n"+words[2] +
          " together'. Using the power of the Force, a Jedi can do many \n"+words[3] +
          " things, like using the Force to exercise "+words[4]+" control over \n"+words[5]+"-minded "+words[6] +
          ". A Jedi can also use the Force to move objects" + " with his or her \n"+words[7] +
          ". It doesn't matter how "+words[8]+" these objects" + " are; it only matters how \n" +
          words[9]+" the Jedi believes in the Force." + "Most importantly, the Force teaches\n"
          "a Jedi to rely on his or her feelings. As Obi-Wan Kenobi told his student, \nLuke "+words[10])


# Resources used:
# https://www.pinterest.com/pin/563724078354382198/
if __name__ == '__main__':
    poem_base(user_input())
