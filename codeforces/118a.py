s = input()
new_s = ''
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for char in s:
    if char not in vowels:
        new_s += '.'
        if ord(char) <= 90:
            new_s += chr(ord(char) + 32)
        else:
            new_s += char
print(new_s)