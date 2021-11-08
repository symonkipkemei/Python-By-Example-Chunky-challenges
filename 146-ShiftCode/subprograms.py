# there are two parameters needed for this programme.
# We are going to create a sub-programme that picks the following items


# MESSAGE
def userMessage():
    """Pick the message for the programme"""
    message = input("enter message : ")

    return message


# NUMBER
def userNumber():
    """Picks the number of times the code should be shifted by"""
    number = int(input("enter number : "))

    return number


# THE ENCODER

def encoder(message, number):
    listMessage = list(message)
    newMessage = []
    editedMessage = []

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets = list(alphabets)
    for y in listMessage:
        for index,x in enumerate(alphabets):
            if y == x:
                point = index
                newMessage.append(point)
    print(newMessage)


    #decoding by the number

    for z in newMessage:
        editedNumber = int(z)+number
        editedMessage.append(editedNumber)

    print(editedMessage)



# DECODING


def main():
    message= userMessage()
    number = userNumber()

    encoder(message, number)

main()