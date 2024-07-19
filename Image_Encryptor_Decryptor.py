from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    key_array = np.frombuffer(key.encode('utf-8'), dtype=np.uint8)
    key_array = np.resize(key_array, image_array.shape)
    encrypted_array = image_array ^ key_array
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save("Encrypted_image.png")

def decrypt_image(image_path, key):
    encrypted_image = Image.open(image_path)
    encrypted_image_array = np.array(encrypted_image)
    key_array = np.frombuffer(key.encode('utf-8'), dtype=np.uint8)
    key_array = np.resize(key_array, encrypted_image_array.shape)
    decrypted_array = encrypted_image_array ^ key_array
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save("Decrypted_image.png") 



def main():

    try:
        print(r"""
               +============================================================+
               |   ___              ___                       _             |
               |  |_ _|_ __  __ _  | __|_ _  __ _ _ _  _ _ __| |_ ___ _ _   |
               |   | || '  \/ _` | | _|| ' \/ _| '_| || | '_ \  _/ _ \ '_|  |
               |  |___|_|_|_\__, | |___|_||_\__|_|  \_, | .__/\__\___/_|    |
               |            |___/                   |__/|_|                 |
               +============================================================+
           """)
        while True:
            enc_dec = input("Type '-e' to encrypt or type '-d' to decrypt the image. Type 'quit' to exit the program. : ")
            if enc_dec == '-e':
                image_path = input("Give image Path : ")
                key = input("Enter the key value with which the image has to be encrypted (The Key can be Alphanumeric) : ")
                encrypt_image(image_path, key)
                print("Image has been encrypted and stored !")
            elif enc_dec == '-d':
                image_path = input("Give image Path : ")
                key = input("Enter the key value with which the image has to be decrypted : ")
                decrypt_image(image_path, key)
                print("Image has been decrypted and stored !")
            elif enc_dec.lower() == 'quit':
                print("Byeee.....")
                exit()
            else:
                print("Invalid option!!! , Try Again.")
    except FileNotFoundError as FN:
        print(f"File doesn't seem to exist at the given location with the error code {FN}")
    except KeyboardInterrupt:
        print("\nByeee.....")


if __name__ == "__main__":
    main()