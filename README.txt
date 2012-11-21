Six_Tweets_of_Separation
========================
What Python libraries need to be installed:
	* numpy
	* scipy
	* ujson
	* pymongo
	* nose

How to run tests:
	* Extract all the files from this repo
	* Change directory to this folder
	* Run this line:
		$ nosetests
	* This will run the files in the \tests folder

How to run dijkstra.py:
	* To run dijkstra.py, run this line:
		$ python dijkstra.py <file_name>.json
	* <file_name>.json is the name of the single line dictionary in a json file
	* To see how this runs, run this line:
		$ python dijkstra.py dijkstra_example.json
	* You will be prompted by the line
		$ Enter Start Point: 
	* For this example type "O" (the letter; without quotes)
	* You will be prompted by the line
		$ Enter End Point: 
	* For this example type "T" (without quotes)
	* You should see this line
		$ ['O', 'A', 'B', 'D', 'T']
	* If you make your own graph, look at dijkstra_example.json and dijkstra.py for example and explanation

How to run hits.py:
	* To run dijkstra.py, run this line:
		$ python hits.py <file_name>.json
	* <file_name>.json is the name of a json file containing tweets with user mentions
	* The tweets in the file are dictionaries and must have a key of "text" and "screen_name"
	* To see how this runs, run this line:
		$ python hits.py hits_example.json
	* If you make your own tweets, look at hits_example.json for examples
	