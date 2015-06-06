#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from bayes import classify
from t2l import txt_to_list

reload(sys)
sys.setdefaultencoding('utf8')

def final_result(text):

	result = classify(text)

	if result < 0.35:
		return "Positive"
	elif result>0.65:
		return "Negative"
	else:
		return "Neutral"



