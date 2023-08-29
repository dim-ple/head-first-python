phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# Removes our last 4 values
for i in range(4):
    plist.pop()

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join(plist[5:3:-1]) + ''.join(plist[7:5:-1])

print(plist)
print(new_phrase)
