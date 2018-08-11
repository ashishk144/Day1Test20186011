'''
    Assignment-1 Create Social Network
'''
net_dict = {}
def create_social_network(inp_line):
    '''
    The data argument passed to the function is a string
    It represents simple social network data
    In this social network data there are people following other people

    Here is an example social network data string:
    John follows Bryant,Debra,Walter
    Bryant follows Olive,Ollie,Freda,Mercedes
    Mercedes follows Walter,Robin,Bryant
    Olive follows John,Ollie

    The string has multiple num_lines and each line represents one person
    The first word of each line is the name of the person
    The second word is follows that separates the person from the followers
    After the second word is a list of people separated by ,

    create_social_network function should split the string on lines
    then extract the person and the followers by splitting each line
    finally add the person and the followers to a dictionary and
    return the dictionary

    Caution: watch out for trailing spaces while splitting the string.
    It may cause your test cases to fail although your output may be right

    Error handling case:
    Return a empty dictionary if the string format of the data is invalid
    Empty dictionary is not None, it is a dictionary with no keys
    '''
    while inp_line:
        inp_line = inp_line.readline()
        inp_line = replace("\n","")
        net_dict[inp_line[0]] = inp_line[1].split(",")
    print(net_dict)

def main():
    '''
        handling testcase input and printing output
    '''
    store_string = ''
    num_lines = int(input())
    for i in range(num_lines):
        i += 1
        store_string += input()
        store_string += '\n'
    print(store_string)
    print(create_social_network(store_string))

if __name__ == "__main__":
    main()