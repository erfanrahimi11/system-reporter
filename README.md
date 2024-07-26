This project is a RAM memory monitoring system for Windows and Linux operating systems, etc. In this project, the values ​​of used memory (Used), free memory (Free) and total memory (Total) are stored every minute and are accessible through an API. This API can return a specified number of last saved records as JSON.

Project structure backend.py: a script that reads RAM memory information every minute and stores it in the database. main.py: An API created using the FastAPI framework that allows users to retrieve a specified number of the last records stored in the database as JSON. memory_data.db: sqlite database that stores memory information.

Installation:

    prerequisites: Python 3.8 or higher
    pip (Python package manager)

Returned JSON structure The API response consists of a list of JSON objects, each of which displays information about RAM memory usage over a specified time period. Each object contains the following fields:

timestamp: the time when the information was recorded as a Unix timestamp (seconds since January 1, 1970). total: the total amount of RAM available in the system (in megabytes). free: The amount of RAM that is currently free and usable for applications (in MB). used: The amount of RAM memory that is being used by system programs and processes (in megabytes).
