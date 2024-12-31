def reverse_each_word(string):
    words=string.split()
    print(words)
    reversed_words=[word[::-1] for word in words]
    return ' '.join(reversed_words)
input_string="yamini durga"
output_string=reverse_each_word(input_string)
print(output_string)