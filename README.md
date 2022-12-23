# Famliy_Tree
Hackathon Problem Statement

Build a National Family Tree 🏡

👷👷‍♀️ WHAT TO BUILD

Create a Family Tree of all families in India (Pan India) using Electoral Roll Pdf with the data available at nsvp.in.

You can use any technology or any hack to crack the following problem statement.

Below are steps to generate Electoral Roll with any person’s data:
Head over to Generate Voter Information and fill in the required information


This will generate a list of users with the following name. Select the one from the following.



Click on view details, and this will take to a new page with details like:
Assemble Constituency
EPIC no. (Voter Card No.)
Part Number
Serial No.



















      4. Next, head over to Generating Electoral PDF, and select the state taking data from Person’s data, as shown above.


     5. Every state website will have a section with Electoral Roll, click on that



    6. Enter the District and AC (Assembly Constituency) from the previous data


















   7. It will give you a list of Electoral PDFs for all the polling stations:



   8. From the AC and Part Number found from the previous record, we find our polling station


   9. From the Serial Number we had with us, we can find the person from the list and we can find families living in the same house, and following we can dig deep in the family tree.


Here is a small walkthrough video for reference:  
https://drive.google.com/file/d/1ocNhLxbTbEwGdFkpjoRrr4BStS21fwIN/view     



⁉️ WHAT ARE THE CONSTRAINTS?
Absolutely nothing. You are free to use any open-source libraries or build solutions from scratch. 

WHAT DO YOU HAVE TO MAKE?
Create an API, which takes some or all parameters:
Name
Age
Address
City
State
Local Area
Voter ID
Gender
We don’t want to restrict you to these parameters. Feel free to dive in more.
and returns:
Family Tree of the Individual with labelled relations. (Whatever format suits your execution)

Sample Response:

Input
{ “name”: “shyam Murugan”, “age”: 21 }

Output
{ “persons”: [ { “name”: “abcd efgh”, “relation”: “self” }, {“name”: “xyz ”, “relation”: “parent”}, {“name”:  “blee “, “relation”:  “parent”}]}

WHAT WE NEED?
Host the API with the Postman with sample responses with different parameters.
Generate a PDF/Json/Zip etc (Any format) of family tree of all families in India. (Brownie Points)

Make sure the extracted result has been translated to English from 
whatever regional language they might be in.

JUDGES
BharatX Team will be going through all the submissions.

JUDGING CRITERIA
Accuracy:
How many number of families is your solution able to collect?
How accurate your solution produces a family tree?
Creativity: (Out of the Box Thinking)

WHERE TO SUBMIT
Submit through the Submit button’s Description Link, which is a gform. (On the unstop page)
Note: To be submitted by only one person from the team.
Host your solution on a cloud platform like AWS, Google Cloud, Microsoft Azure or any other platform of your choice and submit the cloud deployment via creating a Postman Collection. Make sure that the collection is accessible publicly. (Create a public Workspace). 
Postman - 
https://www.postman.com/downloads/
https://learning.postman.com/docs/getting-started/creating-the-first-collection/





