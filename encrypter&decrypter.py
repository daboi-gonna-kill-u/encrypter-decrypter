#this function will convert each letter of the message variable 
#and will change its ascii value to one above and will replace 
#the original letter with the new ascii value as text
def encryption(message,key):
    output = ''
    for i in range(len(message)):
        ascii_message_add = ord(message[i])+ key
        output = output + chr(ascii_message_add)
    return output

def decryption(enc_message,key):
    output = ''
    print(len(enc_message))
    for i in range(len(enc_message)):
        ascii_message_add = ord(enc_message[i])- key
        output = output + chr(ascii_message_add)
    return output


what_are_we_doing = int(input('do you want to encrypt or decript? Enter 1 for encryption and 2 for decryption : '))
if what_are_we_doing == 1:
    message = input('write your message here: ')
    key = int(input('enter a number as your key: '))
    print(encryption(message,key))
elif what_are_we_doing == 2:
    enc_message = input('paste your encrypted message here: ')
    key = int(input('enter your key: '))
    print('this should be your decryped answer according to your key: ',decryption(enc_message,key))
