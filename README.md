College Recommendation System using AI Pipeline: For PrathamAI Hackathon '24
==============================================

Overview
--------

This is a Python script that uses the AIXplain API to recommend colleges based on a user's grades and extracurricular activities. The script takes in user input for various academic and extracurricular parameters, constructs a query, and sends it to the AIXplain API. The API then returns a list of recommended colleges along with their advantages and disadvantages.

How it Works
-------------

### 1. Importing Required Libraries

The script starts by importing the necessary libraries:

* `os` for system-level operations
* `requests` for making HTTP requests to the AIXplain API
* `datetime` for date and time-related operations

### 2. Setting up the Environment

The script sets up the environment by:

* Clearing the terminal screen using `os.system("cls" if os.name == "nt" else "clear")`
* Setting an environment variable `TEAM_API_KEY` with a predefined API key

### 3. Installing AIXplain Library (if necessary)

The script checks if the `aixplain` library is installed. If not, it installs it using `pip install aixplain`.

### 4. Creating a Pipeline Factory

The script creates a `PipelineFactory` instance using the `aixplain` library and sets up a pipeline with the API key.

### 5. Defining User Input Parameters

The script defines various user input parameters:

* `gpa`
* `math_grade`
* `science_grade`
* `english_grade`
* `world_language`
* `ap_courses`
* `honors_courses`
* `sat_score`
* `volunteer_hours`
* `extracurricular_activities`
* `country`

### 6. Constructing the Query

The script constructs a query using the user input parameters and sends it to the AIXplain API.

### 7. Running the Pipeline

The script runs the pipeline using the `pipeline.run(query)` method and retrieves the response from the AIXplain API.

### 8. Parsing the Response

The script parses the response and extracts the recommended colleges along with their advantages and disadvantages.

### 9. Printing the Output

The script prints the output in a formatted manner using Markdown.

How to Run
----------

To run this script, follow these steps:

1. Install the required libraries by running `pip install os requests datetime aixplain`
2. Set up your AIXplain API key by replacing the `TEAM_API_KEY` variable with your own API key
3. Run the script using `v1_frontend.py`
4. Follow the prompts to input your academic and extracurricular parameters
5. The script will print out a list of recommended colleges along with their advantages and disadvantages

**Note:** Make sure to replace the `TEAM_API_KEY` variable with your own AIXplain API key. The API Key provided is a fake placeholder.
