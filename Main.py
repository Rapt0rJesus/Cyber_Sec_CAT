from Chinese_Remainder import CRT
from Euclidean_GCD import Extended_Euclidean, Euclidean_GCD
from Miller_Rabin import Miller_Rabin
import Ciphers
from ECC import ECC
from ElGamal import Elgamal
from RSA import RSA

while(True):
    a = int(input('''
    
    Enter your choice 
    1- Chinese Remainder Theorem
    2- Euclidean GCD
    3- Extended Euclidean Inverse
    4- Miller Rabin Primality test
    5- Caeser Cipher
    6- vigenere cipher
    7- Row Transpose Cipher
    8- RSA ready to go
    9- Diffie Hellman ECC cryptography
    10- Elgamal cryptography

    You can't escape this terminal, I'm too lazy so just keep pressing Ctrl+C if you want to exit.
    Hi, the author of the code just wants to see you succeed, so he prays for you that this comes helpful in yor CAT. 
    Everyone can use a bit of support in such times, so smile and do your best to make others smile :3.
    42 is the answer :)

    Enter your choice: '''))
    if(a == 1):
        n = int(input("enter number of equations: "))
        CRT(n)
    elif(a == 2):
        n1 = int(input("Enter first number: "))
        n2 = int(input("enter second number: "))
        print(Euclidean_GCD(n1, n2))
    elif(a == 3):
        v = int(input("enter number to find inverse of: "))
        m = int(input("Enter number with respect to find inverse to(modulo): "))
        result = Extended_Euclidean(m, v)
        print("Final result is: \t", result)
    elif(a == 4):
        n = int(input("enter number to check: "))
        b = int(input("Enter base value: "))
        result = Miller_Rabin(n, b)
        print("Final result is : \t", result)
    elif(a == 5):
        s = input("Enter string to encode: ")
        n = int(input("enter shift: "))
        result = Ciphers.Caesar(s, n)
        print("Final result is:\t", result)
    elif(a == 6):
        s = input("Enter string to encode: ")
        k = input("Enter key: ")
        result = Ciphers.vigenere(k, s)
        print("final result is: \t", result)
    elif(a == 7):
        s = input("Enter string to encode: ")
        k = input("Enter key: ")
        Ciphers.Row_transpose(k, s)
    elif(a == 8):
        RSA()
    elif (a == 9):
        ECC()
    elif(a==10):
        Elgamal()
