from sys import argv

script,file_name = argv

print "We'r going to erase %r." % file_name

print "If you dont want that, hit CTRL-C(^C)"

print "If you want that, hit RETURN"

raw_input("?")

print "OPening the file..."
target = open(file_name,'w')

print "Trucating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three Line "

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally we have to close it"

target.close()