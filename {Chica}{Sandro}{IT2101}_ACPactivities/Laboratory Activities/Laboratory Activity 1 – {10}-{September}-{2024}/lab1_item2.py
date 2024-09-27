# Function to find and display the character with the larger value based on its ASCII Values
def compare_characters():
    # Prompt user to enter two characters
    chars = input("Enter two space-separated characters: ").split()
    
    # Get the character with the larger value
    larger_char = max(chars[0], chars[1])
    
    # Output the result
    print("----------------------------------")
    print(f"The character with greater value is: {larger_char}")
    print("----------------------------------")
    
    # Show ASCII values
    for char in chars:
        ascii_val = ord(char)
        print(f"{char}:{ascii_val}")

# Call the function
compare_characters()
