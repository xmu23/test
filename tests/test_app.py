from app import index


def test_about():
	
	# simple way to test webpage (words for basic pages)
	assert about() == "About us: Naser and the cool kids from CS321"

	# more intreesting way to test the the page works
	client = app.test_client()
	response = client.get("/about")
	assert response.status_code == 200  # success