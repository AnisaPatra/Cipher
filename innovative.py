import random
import string

def autokey(text):
    letters = string.printable
    random_str = ''.join(random.choice(letters) for i in range(len(text)))
    key =''.join(random.sample(random_str,len(random_str))) 
    return key


def encrypt(text, key,n):
      result = "";
      ptr = 0;
      for char in text:
            result = result + chr(ord(char) ^ ord(key[ptr]) * n)
            ptr = ptr + 1;
      res = ' '.join(format(ord(i), 'b') for i in result)
      return res[::-1]


def decrypt(text,key,n):
      text = text[::-1]
      string = "".join([chr(int(i, 2)) for i in text.split(" ")])
      result = "";
      ptr = 0;
      for char in string:
            result = result + chr(ord(char) ^ ord(key[ptr]) * n)
            ptr = ptr + 1;
      return result


    
input_text = input("\nEnter Text To Encrypt:\t");
n = random.randint(0,10000)
key = autokey(input_text);
print("Random string is:",key)


encryption = encrypt(input_text, key,n);
final= " "
for i in encryption.split(" "):
    i = int(i)
    final = final + oct(i)
print("\nEncrypted Vernam Cipher Text:\t" + final);
                    
decryption = decrypt(encryption, key,n);
print("\nDecrypted Vernam Cipher Text:\t" + decryption);
