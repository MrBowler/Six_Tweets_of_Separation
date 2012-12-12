Six_Tweets_of_Separation
========================
What Python libraries need to be installed:
	* numpy
	* scipy
	* ujson
	* pymongo
	* nose
	* networkx
	* wx

How to run tests:
	* IMPORTANT: DELETE dijkstra_tests.py BEFORE RUNNING THE NOSETESTS
	* I was having trouble deleting dijkstra_tests.py from the repo
	* Extract all the files from this repo
	* Change directory to this folder
	* Run this line:
		$ nosetests
	* This will run the files in the \tests folder

How to run hits.py:
	* Before running hits.py, open a separate command window and run this line:
		$ C:\mongodb\bin\mongod.exe
	* Keep this window running while running hits.py
	* To run dijkstra.py, run this line:
		$ python hits.py <file_name>.json
	* <file_name>.json is the name of a json file containing tweets with user mentions
	* The tweets in the file are dictionaries and must have a key of "text" and "screen_name"
	* To see how this runs, run this line:
		$ python hits.py hits_example.json
	* If you make your own tweets, look at hits_example.json for examples

How to run find_connection.py:
	* Before running find_connection.py, open a separate command window and run this line:
		$ C:\mongodb\bin\mongod.exe
	* Keep this window running while running find_connection.py
	* To run find_connection.py, run this line:
		$ python find_connection.py
	* In order to run this file, a file called "data.json" must be in the folder
	* "data.json" is created by hits.py
	* Once run, instructions will appear in the command prompt

How to run gui.py:
	* Before running gui.py, open a separate command window and run this line:
		$ C:\mongodb\bin\mongod.exe
	* Keep this window running while running gui.py
	* gui.py is a GUI version of find_connection.py
	* To run gui.py, run this line:
		$ python gui.py
	* Like find_connection.py a file called "data.json" must be in the folder
	* "data.json" is created by hits.py
	* Once run, a window will appear with a layout to use the program