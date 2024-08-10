def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        print("-- Begin report of books/frankenstein.txt ---")
        print(f"{get_number_of_words(file_contents)} words found in the document")

        print()

        characters_count_dict = count_characters_dict(file_contents)
        characters_count_list = count_characters_list(characters_count_dict)

        for character_count in characters_count_list:
            character = character_count["character"]
            num = character_count["num"]
            print(f"The '{character}' character was found {num} times")

        print("--- End report ---")

def get_number_of_words(text):
    words = text.split()
    return len(words)

def count_characters_dict(text):
    characters_dict = {}
    lowered_text = text.lower()

    for character in lowered_text:
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1

    return characters_dict

def count_characters_list(dict):
    result = []

    for pair in dict:
        if pair.isalpha() :
            pair_dict = {
                "character": pair,
                "num": dict[pair]
            }
            result.append(pair_dict)

    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(dict):
    return dict["num"]

main()