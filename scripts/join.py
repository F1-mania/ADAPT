import re
import os
import sys

if __name__ == '__main__':
	cleaned_file = open("joinedtext.txt", 'w')
	counter = 0
	for folder, subs, files in os.walk("./tweets_db"):
		for file_name in files:
			clean_file = open("./tweets_db/" + file_name)
			for line in clean_file:
				new_line = []
				line = line.split()
				for word in line:
					sent = True
					new_word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word)
					if len(new_word) > 1 and new_word != '' and sent:
						new_line.append(new_word)
				new_line.append("\n")
				cleaned_file.write(" ".join(new_line))
				counter += 1
	cleaned_file.close()
	print counter