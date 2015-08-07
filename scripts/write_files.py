import os
import sys

if __name__ == '__main__':
	counter = 1
	os.mkdir("tweet_file")
	reader = open("selected_sents.txt")
	for line in reader:
		print "\rwriting file: " + str(counter),
		writer = open("tweet_file/tweet-" + str(counter).zfill(4) + ".txt", 'w')
		writer.write(line)
		counter += 1

