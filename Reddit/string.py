def find_non_repeating_character(str):
    
    pass
find_non_repeating_character("hello")
find_non_repeating_character("zzxxcvvs")

def check_if_anagram_recursive(str1, str2):
    if(str1 is "" and str2 is ""):
        print("Success")
        return True
    if (len(str1) is not len(str2)):
        print("Failure: Words don't have the same size/length")
        return False
    for letter in str1:
        match = str2.find(letter)
        if(match < 0):
            print("Failure: " + letter + "not found in other string")
            return False
        else:
            _str1 = str1.replace(letter,"")
            _str2 = str2.replace(letter,"")
            return check_if_anagram_recursive(_str1, _str2)
def check_if_anagram(str1,str2):
    # only need to check for this once
    if(str1 is str2):
        print("Failure: a word is not an anagram of itself")
        return False
    check_if_anagram_recursive(str1,str2)
# check_if_anagram("", "c")

def check_all_are_unique(str):
    for letter in str:
        index = str.find(letter)
        if(index is 0):
            test=str[1:len(str)]
        elif(index is len(str)):
            print("all are unique")
            return True
        else:
            test = str[0:index-1] + str[index+1:len(str)]
        print(test)
        if letter in test:
            print("letter found :(")
            return False
    print("all are unique")
    return True
check_all_are_unique("helsakdjjsnklclddlkslknsadkljskljdo")