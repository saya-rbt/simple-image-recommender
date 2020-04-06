# Simple image recommender
#
# required:
# data/images: a folder containing your images dataset
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

# Main function
def main():
	print("Loading...")
	print(" -- Looking up images...")
	# TODO
	print(" -- Calculating color clusters (this can take some time)...")
	# TODO
	print(" -- Extracting tags...")
	# TODO
	print("Loading done!")

	# Gathering user data
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
		user_favs.append(input("Please enter the images you want to add, separated by a comma: ").split(","))
	do_dislike = input("Would you like to define your disliked images? ([y]es/[n]o/[a]dd): ")
	if do_dislike == "y":
		user_dislikes = input("Please enter your disliked images, separated by a comma: ").split(",")
	elif do_dislike == "a":
		user_dislikes.append(input("Please enter the images you want to add, separated by a comma: ").split(","))
	print(user_favs)
	print(user_dislikes)
	with open("data/users/" + name + ".txt", "w+") as userfile:
		userfile.write(",".join(user_favs) + "\n")
		userfile.write(",".join(user_dislikes) + "\n")

	# Recommendation system
	print("Computing recommendation...")
	# TODO

main()