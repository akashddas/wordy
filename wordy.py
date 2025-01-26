import sys
import os


def sort_on(dict) -> int:
    return dict["num"]


def words(file) -> int:
    with open(file) as f:
        file_contents = f.read()
        word_count = file_contents.split()
        return len(word_count)


def characters(file) -> dict:
    char_count = {}
    with open(file) as f:
        file_contents = f.read()
        for word in file_contents.lower().split():
            for character in word:
                if character.isalpha():
                    # TODO: Simplify this logic
                    if character in char_count:
                        char_count[character] += 1
                    else:
                        char_count[character] = 1
        return char_count


def report(file) -> None:
    char_list = []
    char_count = characters(file)
    for char, num in char_count.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {sys.argv[2]} ---")
    print(f"{words(file)} found in the document\n")
    for char_data in char_list:
        print(f"The '{char_data["char"]}' character was found {
              char_data["num"]} times")


def main() -> None:
    if len(sys.argv) < 3:
        print("wordy: missing option flag or directory argument")
        sys.exit(1)

    if not sys.argv[1]:
        print("wordy: missing option flag")
        sys.exit(1)

    if not sys.argv[2]:
        print("wordy: missing option dir")
        sys.exit(1)

    if not os.path.exists(sys.argv[2]):
        print(f"wordy: {(sys.argv[2].split("/"))[-1]} file not found")
        sys.exit(1)

    else:
        match sys.argv[1]:
            case "-w":
                word_count = words(sys.argv[2])
                print(word_count)
            case "-c":
                char_count = characters(sys.argv[2])
                print(char_count)
            case "-r":
                report(sys.argv[2])
            case _:
                print(f"wordy: invalid option '{sys.argv[1]}'")


if __name__ == "__main__":
    main()
