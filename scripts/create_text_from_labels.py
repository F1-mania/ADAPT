import sys
import os

if __name__ == '__main__':
	writer = open('prompt_list.txt', 'w')
	reader = open('./tweet_file/tweet1.data')
	for line in reader:
		line = line[16:-4]
		writer.write(line + "\n")
	reader = open('./tweet_file/tweet2.data')
	for line in reader:
		line = line[16:-4]
		writer.write(line + "\n")
	writer.close()