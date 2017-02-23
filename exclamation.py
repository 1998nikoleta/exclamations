print "WELCOME!!!"
sentence= raw_input ("Please give a sentence with exclamation marks:")
count=sentence.count("!")-1
sentence = sentence.replace('!','',count)
print sentence



raw_input("Press <enter> to exit")
