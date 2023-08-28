phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# Removes our last 4 values
for i in range(4):
    plist.pop()

# Removes the "D" at the beginning of our list
plist.pop(0)

# Specifically removes the apostrophe from the list
plist.remove("'")

# Re-orders the last two values in our list so instead of "pa", we have "ap"
# The pop methods execute first from left to right. Then the walues ["a", "p") are
# are added to the end of the list via the extend method.
plist.extend([plist.pop(), plist.pop()])

# Takes our value at index 3, removes it from the list and returns it to index 2
plist.insert(2, plist.pop(3))


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
