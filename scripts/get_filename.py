import os
import sys

if __name__ == '__main__':
	writer = open('./tweet_file/filenames.txt', 'w')
	files = open("./tweet_file/tweet1.data")
	for filename in files:
		file_name = filename[10:14]
		line = "tweet-" + file_name + ".txt "
		writer.write(line)
