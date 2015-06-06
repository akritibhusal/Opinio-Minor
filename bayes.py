#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import sys, re
from t2l import txt_to_list

#Setting default encoding to utf-8 to support nepali text
reload(sys)
sys.setdefaultencoding('utf8') 

db = MySQLdb.connect("localhost","user","password", "bayes" )
cursor = db.cursor()
cursor.execute("SET NAMES utf8")

def prob_4_word(word):
	PROB_RARE_WORD = 0.5

	sqlSel_pos = "SELECT * FROM `classified` WHERE word = '%s' AND tag = '%s'" % (word, 'p')
	cursor.execute(sqlSel_pos)
	data_pos = cursor.fetchone()

	sqlSel_neg = "SELECT * FROM `classified` WHERE word = '%s' AND tag = '%s'" % (word, 'n')
	cursor.execute(sqlSel_neg)
	data_neg = cursor.fetchone()

	if data_pos:
		pos_count = data_pos[2]
	else:
		pos_count = 1000
	
	if data_neg:
		neg_count = data_neg[2]
	else:
		neg_count = 1000


	if pos_count == 1000 and neg_count == 1000:
		return PROB_RARE_WORD
	else:
		return float(pos_count)/(float(pos_count) + float(neg_count))


def prob_4_list(prob_list):
	prob_product         = reduce(lambda x,y: x*y, prob_list)
	prob_inverse_product = reduce(lambda x,y: x*y, map(lambda x: 1-x, prob_list))

	return float(prob_product)/(float(prob_product) + float(prob_inverse_product))


def classify(text):
	pl = []
	negation_words=['not','dont'] 
	intensifier_words=['very','extremely']

	text = text.replace("'", "")
	text_list = txt_to_list(text)

	for word in text_list:			
		prob = prob_4_word(word)
		pl.append(prob)
		
			
		result=prob_4_list(pl)
		


	for word in text_list:
		for nword in negation_words:
			if nword==word:
				result = 1-prob_4_list(pl)

	return result
