with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    letter_counts = count_letters(text)
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Begin report of books/frankenstein.txt ---")
    for char, count in sorted_counts:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


main()