'''
Attempt at implementing problem 32B at Codeforces (Accepted)

Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

Input
The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).

Output
Output the decoded ternary number. It can have leading zeroes.

'''


def decode(borze: str, borze_characters: dict) -> str:
    start_index = 0
    end_index = 1
    decoded_list = []
    while start_index < len(borze):
        borze_substring = borze[start_index:end_index]
        if (borze_substring in borze_characters):
           #Step through the string, recognize characters, and add them to a new list.
            decoded_list.append(borze_characters[borze_substring])
            start_index = end_index
            end_index = start_index + 1
        else:
            end_index += 1
    return ''.join(decoded_list)

def main() -> None:
    borze_characters = {
        '.': '0',
        '-.': '1',
        '--': '2',
    }
    borze = input()
    decoded = decode(borze, borze_characters)
    print(decoded)

main()
