import re
# allows us to specify the rules for the set of possible strings that we may want to match
def word_count(s):
    # Implement me.
    cache = {}
    
    word_list = re.split('[\s":;,.\-+=/\\\|[\]{}()*^&]+', s.lower())

    for i in word_list:
        if i == "":
            continue
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1


    return cache




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))