from bs4 import BeautifulSoup

soup = BeautifulSoup(open("recipes.html"))

recipe_data = []

recipe_titles = soup.find_all('a', {'class' : 'card-title'})
recipe_fotos = soup.find_all('img', {'class' : 'recipe-card-img full'})
for recipe, foto in zip(recipe_titles, recipe_fotos):
	recipe_data.append([recipe['title'].encode('ascii', 'ignore'),("https://www.yummly.com" + recipe['href']).encode('ascii', 'ignore'), foto['src'].encode('ascii', 'ignore')])

with open("recipe_data.csv", "w+") as file:
	for data in recipe_data:
		print(data)
		file.write(data[0])
		file.write(", ")
		file.write(data[1])
		file.write(", ")
		file.write(data[2])

		file.write("\n")
