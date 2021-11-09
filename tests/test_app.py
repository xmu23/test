from app import *


def test_about():
	
	# simple way to test webpage (words for basic pages)
	assert about() == "About us: Naser and the cool kids from CS321"
