import sys
import os

if __name__ == "__main__":
	reader = open("prompt_list.txt")
	writer = open("final_prompts.txt", 'w')
	for line in reader:
		line = line.lower()
		line = line[:-1]
		line = line[0].upper() + line[1:]
		if line[-1] != ".":
			line = line + "."
		elif line[-1] == "!":
			line = line[:-1] + "."
		writer.write(line + "\n")

	writer.close()
	reader.close()