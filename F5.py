import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

secret_message = ""

def f5_encode_image(input_image_path, secret_message_to_hide, key, output_image_path):
    global secret_message # Use the global variable
    
    image = Image.open(input_image_path)
    secret_message_binary = ''.join(format(ord(char), '08b') for char in secret_message_to_hide)
    np.random.seed(key)
    
    image_array = np.array(image)
    height, width, channels = image_array.shape
    
    if len(secret_message_binary) > height * width * channels:
        print("Error: Secret message is too long for the given image.")
        return
    
    rng = np.random.default_rng(key)
    
    # Embed secret message into the image using the F5 algorithm
    current_bit = 0
    for h in range(height):
        for w in range(width):
            for c in range(channels):
                if current_bit < len(secret_message_binary):
                    pixel_value = image_array[h, w, c]
                    
                    # Generate a random value for embedding
                    random_value = rng.integers(0, 2)
                    
                    # Embed the message bit in the least significant bit
                    new_pixel_value = (pixel_value & 0xFE) | (int(secret_message_binary[current_bit]) ^ random_value)
                    
                    image_array[h, w, c] = new_pixel_value
                    current_bit += 1
    
    encoded_image = Image.fromarray(image_array.astype(np.uint8))

    fig, axs = plt.subplots(1, 2)
    axs[0].imshow(image)
    axs[0].set_title("Before Image")
    
    axs[1].imshow(encoded_image)
    axs[1].set_title("After Image")
    
    encoded_image.save(output_image_path)
    
    plt.show()
    print("Image encoded successfully!")
    
    secret_message = secret_message_to_hide # Update the global variable


def f5_decode_image(encoded_image_path, key):
    global secret_message # Use the global variable
    
    encoded_image = Image.open(encoded_image_path)
    np.random.seed(key)
    
    encoded_array = np.array(encoded_image)
    
    rng = np.random.default_rng(key)
    
    secret_message_bits = []
    for i in range(8 * len(secret_message)):
        h, w, c = i // (encoded_array.shape[1] * encoded_array.shape[2]), (i // encoded_array.shape[2]) % encoded_array.shape[1], i % encoded_array.shape[2]
        pixel_value = encoded_array[h, w, c]
        random_value = rng.integers(0, 2)
        extracted_bit = pixel_value & 1 ^ random_value
        secret_message_bits.append(extracted_bit)
    
    secret_message = ''.join(chr(int(''.join(map(str, secret_message_bits[i:i+8])), 2))
    
    return secret_message # Return the decoded secret message



input_image_path = 'dogg.png'
output_image_path = 'output_image.png'
key = int(input("Enter key for encoding: "))
secret_message = input("Enter secret message for encoding: ")
f5_encode_image(input_image_path, secret_message, key, output_image_path)
print("Image encoded successfully!")


encoded_image_path = 'output_image.png'
key = int(input("Enter key for decoding: "))
decoded_message = f5_decode_image(encoded_image_path, key)
print("Decoded Secret Message:", decoded_message)
