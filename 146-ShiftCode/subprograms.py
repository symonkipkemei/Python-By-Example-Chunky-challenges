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
        for index, x in enumerate(alphabets):
            if y == x:
                point = index
                newMessage.append(point)
    print(newMessage)

    # decoding by the number

    for z in newMessage:
        editedNumber = int(z) + number
        editedMessage.append(editedNumber)

    # displaying the decoded message

    decodedMessage = []

    for x in editedMessage:
        for indexing, y in enumerate(alphabets):
            if indexing == x:
                decodedMessage.append(y)

    ujumbe = ''

    for z in decodedMessage:
        ujumbe += z

    tuple = (ujumbe, alphabets)

    return tuple


# DECODING


def decoder(encoded, alphabets, number):
    """ We are going to decode the message we just coded above"""

    # convert message to index
    msg = []
    for y in encoded:
        for index, x in enumerate(alphabets):
            if y == x:
                msg.append(index)

    newMsg = []

    for z in msg:
        newNo = z - number
        newMsg.append(newNo)

    # change the decoded msg to alphabets
    newMsgWord = []

    for l in newMsg:
        for indexs, x in enumerate(newMsg):
            if l == indexs:
                newMsgWord.append(x)

    msg1 = ""

    for x in newMsgWord:
        msg1 += x
    print(msg1)



def main():
    message = userMessage()
    number = userNumber()

    ujumbe, alphabets = encoder(message, number)

    decoder(ujumbe, alphabets, number)


main()
