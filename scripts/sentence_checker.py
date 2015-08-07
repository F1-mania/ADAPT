import os
import sys
import enchant
from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.model import NgramModel
from nltk.probability import *


if __name__ == "__main__":
	heteronyms = ["affect", 'alternate', 'are', 'ares', 'attribute', 'august', 'axes', 'bass', 'bow', 'bowed', 'buffet', 'close', 'combine', 'conduct', 'conflict', 'console', 'content', 'contest', 'contract', 'convert', 'converse', 'convict', 'crooked', 'deliberate', 'desert', 'digest', 'dove', 'drawer', 'excuse', 'house', 'incense', 'intern', 'invalid', 'laminate', 'lather', 'lead', 'minute', 'moderate', 'mow', 'multiply', 'number', 'object', 'pasty', 'pate', 'perfect', 'periodic', 'permit', 'polish', 'present', 'primer', 'produce', 'project', 'raven', 'rebel', 'record', 'recreation', 'refuse', 'relay','rerun', 'reside', 'resume', 'resign', 'row', 'sake', 'secrete', 'secreted', 'separate', 'sewer', 'slough', 'sow', 'subject', 'tear', 'wind', 'wound']
	dic = enchant.Dict("en_GB")
	inname = input("Select Input File: ")
	infile = open(inname)
	writer = open('selected_sents.txt', 'w')
	word_count = {}
	useful = []

	count = 0

	num_lines = sum(1 for line in open(inname))

	for line in infile:
		seen_twice = 0
		count += 1
		percentage = 100*count/num_lines
		print "\rchecking line: " + str(count) + "         " + str(percentage) +"%", 
		correct_length = False
		no_heteronym = True
		all_in_dict = True
		unique = True
		no_full = True
		line = line.split()
		if len(line) >= 5 and len(line) <= 15:
			for word in line:
				word1 = word
				word = word.lower()
				if "." in word:
					index = line.index(word1)
					if index != len(line) - 1:
						no_full = False
				if word == "RT":
					all_in_dict = False
				if word in heteronyms:
					heteronym = False
				if not dic.check(word):
					all_in_dict = False
				"""if word in word_count:
					if word_count[word] == 5:
						seen_multiple += 1
					else:
						word_count[word] += 1
				else:
					word_count[word] = 1
			if float(seen_multiple)/float(len(line)) == 1.0:
				unique = False"""
			if no_heteronym and all_in_dict and unique and no_full:
				line = " ".join(line)
				if line not in useful:
					useful.append(line)
	print "\ntotal useful sents: " + str(len(useful))

		#train trigram model
	corpus_tokens = []
	print "Adding brown"
	for word in brown.words():
		word = word.lower()
		corpus_tokens.append(word)
	print "Adding gutenberg"
	for word in gutenberg.words():
		word = word.lower()
		corpus_tokens.append(word)
	print "Training Trigram Model"
	lm = NgramModel(3,corpus_tokens,True,False,lambda f,b:LidstoneProbDist(f,0.01,f.B()+1))

	tweet_entropies = []
	count = 1
	for sent in useful:
		sent = sent.split()
		percentage = 100*count/len(useful)
		print "\rChecking entropy : " + str(count) + " of " + str(len(useful)) + "        " + str(percentage) + "%",
		entropy = lm.entropy(sent)
		tweet_entropies.append((" ".join(sent), entropy))
		count += 1
	tweet_entropies.sort(key=lambda x: x[1])
	threshold = int(len(tweet_entropies) * 0.8)
	list_of_tweets = tweet_entropies[:threshold]

	print "\n",

	final_tweets = [a for (a,b) in list_of_tweets]

	count = 1
	for tweet in final_tweets:
		percentage = 100*count/len(final_tweets)
		print '\rWriting: ' + str(count) + " of " + str(len(final_tweets)) + "     " + str(percentage) + "%",
		writer.write(tweet + "\n")
		count += 1
	writer.close()








