def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using Caesar cipher.
    
    Parameters:
        text (str): The input text to process
        shift (int): The number of positions to shift (positive integer)
        mode (str): 'encrypt' or 'decrypt' (default is 'encrypt')
    
    Returns:
        str: The processed text
    """
    if not isinstance(shift, int) or shift < 0:
        raise ValueError("Shift must be a positive integer")
    
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be either 'encrypt' or 'decrypt'")
    
    if mode == 'decrypt':
        shift = -shift # Decrypting is just shifting in the opposite direction
    
    result = []
    
    for char in text:
        if char.isupper():
            # Shift uppercase characters
            shifted = ord('A') + (ord(char) - ord('A') + shift) % 26
            result.append(chr(shifted))
        elif char.islower():
            # Shift lowercase characters
            shifted = ord('a') + (ord(char) - ord('a') + shift) % 26
            result.append(chr(shifted))
        else:
            # Leave non-alphabetic characters as they are
            result.append(char)
    
    return ''.join(result)


# Example usage
if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher Tool")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '3':
            print("Exiting...")
            break
            
        if choice in ['1', '2']:
            text = input("Enter the text: ")
            try:
                shift = int(input("Enter the shift value (positive integer): "))
                if shift < 0:
                    print("Shift must be positive. Using absolute value.")
                    shift = abs(shift)
                
                if choice == '1':
                    encrypted = caesar_cipher(text, shift, 'encrypt')
                    print(f"Encrypted text: {encrypted}")
                else:
                    decrypted = caesar_cipher(text, shift, 'decrypt')
                    print(f"Decrypted text: {decrypted}")
            except ValueError:
                print("Invalid shift value. Please enter a positive integer.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")