def reverseString(s, i = 0) :
    """Reverses the string s recursively """
    if i == len(s):
       return ""

    return reverseString(s, i+1)



print(reverseString("")) # ""
print(reverseString("bonjour")) # ruojnob
print(reverseString("ressasser")) # ressasser
