"""
Implememnt a method to perform basic string string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the 'compressed' string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters(a-z).
"""

def checkstring(s):
    compressedstr = []
    count = 0
    i = 0

    while i < len(s):
        ch = s[i]

        while i < len(s) and s[i] == ch:
            count += 1
            i += 1

        compressedstr.append(ch)
        compressedstr.append(str(count))
        count = 0
        
    resultstr = "".join(compressedstr)

    return resultstr if len(resultstr) < len(s) else s




string = "aabcccccaaa"
print(checkstring(string))
