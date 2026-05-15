# Lab 1 
# 2. Open the file with the 'a' (append) parameter
f = open("about_me.txt", "a")
f.close()

f = open("about_me.txt", "a")

# I Use .write() to add your perfect night out
f.write("\nPerfect night out: I would go to a nice dinner with my family and then see a movie.")

# Close the file
f.close()

