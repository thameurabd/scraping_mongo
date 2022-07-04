import requests


#test get all articles
response_get_all = requests.get("http://localhost:8000/articles")
assert response_get_all.status_code == 200, response_get_all.text
print ("test all articles OK")


#test get article by title
test_title = input("what article are you looking for?")
test_url = "http://localhost:8000/articles/" + requests.utils.quote(test_title)
response_by_article = requests.get(test_url)
assert response_by_article.status_code == 200
print (f"test article {test_title} OK")


