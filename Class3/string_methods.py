s = input("Enter the name of any movie with more than 2 one word:-")
print("Now let's do some twist and turns")
len_string=len(s)
# Length should be 20
print("Length of movie name = {}".format(len_string))

# First occurrence of "a" should be at index 8
occur_t=s.index("a")
print("The first occurrence of the letter a = {}".format(occur_t))

# Number of a's should be 2
count_t=s.count("a")
print("t occurs {} times".format(count_t))

# Slicing the string into bits
s_firstfive=s[:5]
s_fivetoten=s[5:10]
s_lastfive=s[-5:]

print("The first five characters are {}".format(s_firstfive)) # Start to 5
print("The next five characters are {}".format(s_fivetoten)) # 5 to 10
print("The last five characters are{}".format(s_lastfive)) # 5th-from-last to end
# Convert everything to uppercase
print("String in uppercase",s.upper())

# Convert everything to lowercase
print("String in lowercase",s.lower())


# Only first word capital
print("String in lowercase",s.capitalize())
# Convert to a title
print("string in title form",s.title())

# reverse the name

rev_s=s[::-1]
print(rev_s)

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string",s.split(" "))

#trim
print("string in trimmed form",s.strip())

