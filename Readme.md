# Querying APIs with Python
*A workshop for the Art of Data Visualization conference at Columbia University, April 7th 2016. A project by Juan Francisco Saldarriaga (jfs2118@columbia.edu).*

### 1. Brief introduction to Python and APIs
* Intro to APIs
* Examples of things people do with APIs
* Why Python? **Python 2.7 vs Python 3**
* Open a Foursquare [developer account](https://developer.foursquare.com/)
* Copy API key
* Python IDE:
  * Mac:
    * Terminal
    * [Sublime Text](https://www.sublimetext.com/)
    * [Canopy](https://www.enthought.com/products/canopy/)
  * Windows:
    * [Canopy](https://www.enthought.com/products/canopy/)
    * [Anaconda](https://www.continuum.io/downloads)
    * ??????????????????????
* Overview of process and possible outcome
* Talk about authorization process (token vs. 2 step OAuth)

### 2. Basic concepts of programming in Python
* Functions
* Variables:
  * Types of variables
  * Operations between variables:
    * Problems with combining certain kinds of variables together (ie. string + int or float)
  * Global vs. local
* Comments
* Loops
* Conditionals
* Libraries

### 3. Querying the API

#### A. Building the request
1. Import library
2. Build request (string)
3. Submit request
4. Get response
5. JSON format

#### B. Parsing the response
1. Import library
2. Examine response
3. Extract data from response

#### C. Importing base data
1. Open file
2. Reading data from file
3. Building multiple requests with data
4. Handling errors
5. Careful with API rate limits

#### D. Exporting data
1. Creating new file
2. Writing data to new file