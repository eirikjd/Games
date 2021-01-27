arr = [(0,j) for j in range(10)] + [(j,0) for j in range(10)]
#print(arr)
screen_width = 10
screen_height = 10
ss = [(screen_width,i) for i in range(screen_height)]
print(ss)
s

def long_words(lst):
    return [word for word in lst if len(word) > 5]