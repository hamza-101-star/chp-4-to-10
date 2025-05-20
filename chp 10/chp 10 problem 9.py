def count_word_occurrences(filename, word):
    """Count occurrences of a word (case-insensitive) in a text file."""
    try:
        with open(filename, encoding='utf-8') as file:
            text = file.read().lower() 

    except FileNotFoundError:
        print(f"⚠️ The file '{filename}' was not found.")
        return

    total_count = text.count(word)
    print(f"In '{filename}': '{word}' appears approximately {total_count} times.")

filename = 'pride_and_prejudice.txt'
count_word_occurrences(filename, 'the')
count_word_occurrences(filename, 'the ')
