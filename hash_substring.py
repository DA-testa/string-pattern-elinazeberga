# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    choice = input()
    if "I" in choice:
        text = input().strip()
        pattern = input().strip()
    elif "F" in choice:
        with open("./tests/06", "r") as file:
            text1 = file.readline()
            text = text1[1].rstrip()
            pattern = text1[0].rstrip() 
            #nameNum = "tests/" + nameNum

    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurances = []
    pattern_len = len(pattern)
    text_len = len(text)
    for i in range(text_len - pattern_len + 1):
        text1 = text[i:i + pattern_len]
        if hash(pattern) == hash(text1):
            occurances.append(i)

    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return occurances

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

