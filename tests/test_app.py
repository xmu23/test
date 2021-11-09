from app import *


def test_about():
	
	# simple way to test webpage (words for basic pages)
	assert about() == "TOM's Website"
