# Function to gather song details from the user
def collect_song_details():
    # Prompt user for the input
    year = int(input("Enter the year: "))
    genre = input("Enter the genre: ")
    album = input("Enter the album: ")
    title = input("Enter the song title: ")
    artist = input("Enter the artist: ")

    # Print the details in the expected format
    print("-------------------")
    print("SONG DETAILS")
    print("-------------------")
    print(f"Year Released: {year}")
    print(f"Genre: {genre}")
    print(f"Album: {album}")
    print(f'Title: "{title}"')
    print(f"Artist: {artist}")

# Call the function
collect_song_details()
