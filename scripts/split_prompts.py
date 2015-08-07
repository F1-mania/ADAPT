import os
import sys

if __name__ == '__main__':
    os.mkdir("./tweet_prompts")
	reader = open('prompt_list.txt')
	counter = 1
	file_name = "tweet-"
	for line in reader:
		name = "./tweet_prompts/" + file_name + str(counter).zfill(4) + ".txt"
		writer = open(name, 'w')
		writer.write(line)
		writer.close()
		counter += 1