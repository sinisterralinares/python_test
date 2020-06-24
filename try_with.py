try:
    stream = open("output.txt", "wt")
    stream.write("Lorem ipsum dolar")
finally:
    stream.close()  # THIS IS REALLY IMPORTANT!!
# can be written as well as

with open("output.txt", "wt") as stream:
    stream.write("Lorem ipsum dolar my friend")

