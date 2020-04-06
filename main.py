# Simple image recommender
#
# required:
# data/images: a folder containing your images dataset
# data/users: can be empty, but the folder needs to exist (for now ?)
# 
# optional:
# data/tags.csv: a comma-separated list containing the names of your 
# images and the corresponding semicolon-separated tags
# (eg. "37.png,sky;blue;cliff")

# Libraries import
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
from operator import itemgetter
import numpy as np
import pandas as pd
import json
import math
import os

# User data gathering
def user_data_gathering():
	name = input("Please enter your username: ")
	user_favs = []
	user_dislikes = []
	try:
		with open("data/users/" + name + ".txt", "r") as userfile:
			user_favs = userfile.readline().rstrip().split(",")
			user_dislikes = userfile.readline().rstrip().split(",")
	except FileNotFoundError:
		print("This user doesn't exist. Creating it...")
	if not user_favs:
		print("No favourite images defined!")
	if not user_dislikes:
		print("No disliked images defined!")
	do_fav = input("Would you like to define your favourite images? ([y]es/[n]o/[a]dd): ")
	if do_fav == "y":
		user_favs = input("Please enter your favourite images, separated by a comma: ").split(",")
	elif do_fav == "a":
		user_favs += input("Please enter the images you want to add, separated by a comma: ").split(",")
	elif do_fav == "n":
		pass
	else:
		print("Incorrect choice. Exiting")
	do_dislike = input("Would you like to define your disliked images? ([y]es/[n]o/[a]dd): ")
	if do_dislike == "y":
		user_dislikes = input("Please enter your disliked images, separated by a comma: ").split(",")
	elif do_dislike == "a":
		user_dislikes += input("Please enter the images you want to add, separated by a comma: ").split(",")
	elif do_dislike == "n":
		pass
	else:
		print("Incorrect choice. Exiting")
	print(user_favs)
	print(user_dislikes)

	userfile = open("data/users/" + name + ".txt", "w+")
	userfile.write(",".join(user_favs) + "\n")
	userfile.write(",".join(user_dislikes) + "\n")
	userfile.close()

	return user_favs,user_dislikes


# Get all images filenames in data/images/
def get_image_list():
	imagelist = []
	for file in os.listdir("data/images"):
		if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".tif") or file.endswith(".bmp"):
			imagelist.append(file)
	return imagelist

# Get color clusters per image
def get_clusters(filename, n_clusters):
	imgfile = Image.open("data/images/" + filename).convert('RGBA')
	numarray = np.array(imgfile.getdata(), np.uint8)

	clusters = MiniBatchKMeans(n_clusters=n_clusters)
	clusters.fit(numarray)

	npbins = np.arange(0, n_clusters + 1)
	histogram = np.histogram(clusters.labels_, bins=npbins)

	# Sort histogram
	pairs = sorted(zip(histogram[0], histogram[1]), key=itemgetter(0))
	histogram = (np.array([v for v, i in pairs]),
				 np.array([i for v, i in pairs]))

	colors = []

	for i in range(n_clusters):
		j = histogram[1][i]
		colors.append(
			(
				math.ceil(clusters.cluster_centers_[j][0]),
				math.ceil(clusters.cluster_centers_[j][1]),
				math.ceil(clusters.cluster_centers_[j][2])
			)
		)

	return colors

# Returns a pandas dataframe with the tags info
def get_tags(filename):
	try:
		tags_df = pd.read_csv(filename)
	except FileNotFoundError:
		print("No tags have been defined. Ignoring tags.")

	tags_df["tags"] = tags_df.tags.str.split(";")
	return tags_df

# Main function
def main():
	print("Loading...")
	print(" -- Looking up images...")
	imagelist = get_image_list()
	print(" -- Calculating color clusters (this can take some time)...")
	n_clusters = 4
	# clusters = {filename:get_clusters(filename, n_clusters) for filename in imagelist}
	print(" -- Extracting tags...")
	tags = get_tags("data/tags.csv")
	print("Loading done!")

	# Gathering user data
	print("Gathering user data...")
	(user_favs, user_dislikes) = user_data_gathering()

	# Recommendation system
	print("Computing recommendation...")
	# TODO

main()