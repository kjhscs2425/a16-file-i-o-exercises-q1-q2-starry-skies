# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

with open('romeo_and_juliet.txt', "r") as f:
    text = f.read()

    
# Count how many times the word "Juliet" appears
with open("romeo_and_juliet.txt", "r") as f:
    counter = 0
    for line in f:
        if "Juliet" in line:
          counter += 1
    print(counter)
