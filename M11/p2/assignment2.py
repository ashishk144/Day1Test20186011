"""Exercise: Assignment-2
Implement the update_hand function. Make sure this function has no side effects: i.e.,
it must not mutate the hand passed in. Before pasting your function definition here,
be sure you've passed the appropriate tests in test_ps4a.py."""


def update_hand(hand_inp, word_inp):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for char_acters in word_inp:
        hand_inp[char_acters] = hand_inp[[char_acters][0]] - 1
    return hand_inp

def main():
    """input function"""
    in_put = input()
    a_dict = {}
    for _ in range(int(in_put)):
        data = input()
        list_1 = data.split()
        a_dict[list_1[0]] = int(list_1[1])
    data1 = input()
    print(update_hand(a_dict, data1))

if __name__ == "__main__":
    main()
