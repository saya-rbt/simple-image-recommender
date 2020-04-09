# Simple image recommender

## Goal of the project

The goal of the project is to have a user select their favourite images out of any dataset. The program is merely a PoC, and is simply an exercise about how to use CSV files as `pandas` dataframes, how to get color clusters from image files with `PIL`, `numpy` and `sklearn`, and how to predict similar images using machine learning with `sklearn`. The code is made to be as modular and adaptable as possible, as long as you fit the following requirements:

* **Required:**
	* `data/images`: this is where you need to put your images.
	* `data/users`: this folder will hold every user's data. It can be empty, but the folder needs to exist, otherwise it will thrown an exception.
* **Optional:**
	* `data/tags.csv`: you can put tags here. You need to respect a specific format so the program will be able to read and parse it correctly. Here is the format it should look like:
	```csv
	name,tags
	1.png,tag1;tag2
	2.png,tag1;tag3
	...
	```

## Data sources of your training images and licence

We obviously needed an image dataset in order to base our program on. We decided to go with Pokémons images and we used their types as the tags/labels, that we already described in the `tags.csv` description above.

The reason why we decided to use Pokémons is for convenience: Pokémons have very distinct and bright colors, making it easy to differentiate the color clusters. We didn't particularly used copyright-free images but the program should work with any image dataset anyway in theory, though we didn't test it. Also, Pokémons are cool.

We didn't ask our users to label the images out of convenience too, though we do ask them to select their favourite images to base our predictions on.

## Machine learning models that you tested and used as well as their precision

In order to predict the images the user is likely to like, we used a `RandomForestClassifier`. There are two reasons behind that decision:
* It fit our needs of using our color clusters to predict the images likely to be liked pretty well, and
* We were already familiar with it.

![Random forest classifier](https://miro.medium.com/max/5752/1*5dq_1hnqkboZTcKFfwbO9A.png)

## Size of your training data and test data

Ultimately the size of our training data depends on the user, since the user is choosing the pictures they like. But for the sake of testing, we tried using 150 pictures for our training data, which is basically the first Pokémon generation, minus Mew.

Our test data basically consists of every other image of our dataset, so every Pokémon starting from Mew and up to the 6th generation, which consists of 721 - 150 = 571 images.

We did not decide to use online machine learning for this, everything is done locally on the user's machine. Calculating the clusters can take some time depending on the user's CPU (and also, since it's merely a PoC, it's only mono-thread for now), but with an old i7 running at 2.6 GHz it takes roughly 3 minutes to calculate every picture's color clusters, and a few more seconds to calculate the predictions, which is very acceptable in our opinion.

## Informations stored for every image

For every image, we calculate the 3 more dominant colors (the 3 main color clusters). We store them in a dictionary consisting of the picture's name as key and a list of RGB 3-items tuples as value. If the clusters haven't been calculated yet, they will be calculated at first launch. They will then be saved in a JSON file to save loading time for the next time the program is launched, by reading it rather than recalculating everything at launch.

## Informations concerning user preferences

Every user has a user profile, that can be found in `data/users`. At launch, the user will be asked to enter their name, and the program will attempt to load that user's data. Here's what happens next:
* If it can't find it, the program will create a new one,
* If the user profile exists, it will load it.
The user then has the choice to either overwrite their preferences, edit them, or do nothing and continue as is.

The user profile is stored this way: the first line is a comma-separated list containing the user's favourite images, and the second one is also a comma-separated list except it contains the user's disliked images. We will use the latter in order to predict the user's preferences more accurately, and not recommend images to the user if the user already dislikes them.

## Self-evaluation of your work, remarks and scope for improvement

In my honest opinion, this is still very rudimentary. Though we do have sometimes accurate predictions when using a big enough testing dataset (we regularly have the picture `151.png` recommended when we put the 150 first Pokémons as test set, meaning the last Pokémon of the first generation is likely to be liked by the user), the program could recommend more images (we end up with around 4-5 recommendations out of 571 images). There is plenty of room for improvement, but unfortunately due to our lack of time and knowledge on the topic this is around the best we can do. Maybe more classes on the topic of machine learning/documentation could've been useful, but it's the best we did regarding the situation.

There are also plenty of uncaught exceptions and bugs here and there regarding the user input handling, but again this is mostly due to the lack of time. More work on this program could definitely have resulted in a more polished final result, but as it's merely a PoC, we decided to focus more on the functionalities themselves at first.

**This is definitely not perfect, nor even "production"-ready**, but at least it was a very interesting exercise.

## Conclusion

**Again, this is still merely a PoC used as an exercise to train ourselves to use image manipulation and machine learning.** It is very rudimentary but it quite works, and helped us learn more about data mining and machine learning and the real-life tools used in this field.