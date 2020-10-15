#a,b parameters
def add(a,b):
    sum=a+b
    return sum

#arguments
my_sum=add(100,300)
print(my_sum+50)

def multiply(x,y):
    multiple=x*y
    return multiple

my_multiple=multiply(13,14)
print(my_multiple)

#action based function
def greetings(daytime,name):
        print("Good {} {} .How are you today!".format(daytime,name))

greetings("afternoon","Anu")
greetings("morning","Srijan")

my_word="Pen"
rev_word=my_word[::-1]
print(rev_word)

def rev_word(word):
    my_rev_word = word[::-1]
    return my_rev_word

print(rev_word("abcdefghijk"))

