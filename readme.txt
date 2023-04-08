# Application Name
RAVEN is an application designed to help post-secondary students keep track of assignments and deliverables for several concurrent courses. It provides a centralized platform that allows students to easily manage their assignments, including prioritization, weighting, deadlines, and sources of information. The application provides a calendar interface, allowing students to visualize which deadlines are approaching and display their current lecture and lab times. 
In addition to the 'Student' user account type, there is also a 'Teacher' account type. The 'Teacher' account type is a support role for the student account and has the ability to add course information to the system, allowing students to quickly populate their calendar with class time and deliverable information by 'enrolling' in a course.


## Technologies

The application is built using the LAMP stack, which consists of Linux, Apache, MySQL, and Python. Python is used as the programming language for the application, and MariaDB is used as the database solution. Git or GitHub is used as the version control tool for the application.


## Build and Installation

The build and installation process for this application involves setting up the necessary devices and configuring them to work together. Here are the steps to follow:

1. Set up the Dolphin server
1.1. Install Apache web server and MariaDB on the Dolphin server.
1.2. Create a database schema in MariaDB to hold the data for the application.
1.3. Create a MySQL user with appropriate permissions to access the schema.

2. Set up the cub machine
2.1. Install Python on the cub machine.
2.2. Clone the Raven Application code from the GitHub repository onto the cub machine.
2.3. Install the required Python libraries by running pip install -r requirements.txt in the root directory of the application.

3. Configure the Apache web server
3.1. Copy the contents of the public_html directory from the Raven Application code to the appropriate directory on the cub machine.
3.2. Configure Apache to serve HTML from the public_html directory on the cub machine.

4. Configure the application
4.1. Modify the configuration file to specify the database connection details.
4.2. Run the script to create the necessary database tables.

5. Start the application
5.1. Start the Python application server by running python python server.py in the root directory of the application.
5.2. Access the application by navigating to the appropriate URL in a web browser.

## Usage

1. Configure the application
1.1. Modify the configuration file to specify the database connection details.
1.2. Run the script to create the necessary database tables.

2. Start the application
2.1. Start the Python application server by running python app.py in the root directory of the application.
2.2. Access the application by navigating to the appropriate URL in a web browser.


## Contributors
Austin Shouli
Ethan Ondzik
Ruochi Wang
Anandita Gupta
Vladislav Mazur



## License

Copyright <2023> <Team 4>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
