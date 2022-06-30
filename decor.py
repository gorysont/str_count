import re


SENTENCE = "It is a sentence with a repeating 'a'. And a couple more words."

def preparation(arg):
    """Removing special characters from string"""
    estr = re.sub("[^a-zA-Z ]","", arg).lower().split()
    return estr

def decorator(darg):
    """Checking a counter work"""
    def inner(func):
        def checker(arg):
            test_dict = {}
            for i in set(darg):
                test_dict[i] = int(darg.count(i))
            assert test_dict == func(arg), "Strings aren't equal"
        return checker
    return inner

@decorator(preparation(SENTENCE))
def counting(arg):
    """Counting words for sentence"""
    words = {}
    for i in preparation(arg):
        words[i] = words[i] + 1 if i in words else 1
    return words

counting(SENTENCE)

# add new entry
