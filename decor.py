import re


sentence = "It is a sentence with a repeating 'a'. And a couple more words."

def preparation(arg):
    rem_non_alph = re.compile("[^a-zA-Z ]")
    upd_sent = rem_non_alph.sub("", arg) # delete non-alphabetical chars
    upd_sent = upd_sent.lower() # to count unique words (e.g. A == a)
    global splitting
    splitting = upd_sent.split() # the list with words to count them
    global counts
    counts = []
    global rem_repeat
    rem_repeat = list(dict.fromkeys(splitting)) # remove repeats

preparation(sentence)

def decorator(key, value):
    def inner_func(func):
        def checker(arg):
            counts = {}
            for i,n in zip(key, value):
               counts[i]=n
            if counts == func(arg):
                return func
            return print("Strings' word count don't equal.")
        return checker
    return inner_func

@decorator(rem_repeat, [splitting.count(i) for i in rem_repeat])
def counting(arg):
    words = {}
    words_list = []
    uniq = len(rem_repeat)
    for i in rem_repeat:
        words[i]=int(splitting.count(i))
    print(arg)
    for key, value in words.items():
        words_list.append(value)
        if value == 1:
            print(f"Appears 1 time: '{key}'")
        else:
            print(f"Appears {value} times: '{key}'")
    total = sum(words_list)
    if total == 1:
        print("Only: 1 word.")
    else:
        print("Total:", total, "words.")

    print("Unique words:", str(uniq) + ".")
    return words

counting(sentence)

