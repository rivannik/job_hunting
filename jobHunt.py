import requests
import urllib.request
import time
from bs4 import BeautifulSoup

query = "programmer" #type of job
location = "West Yorkshire" #job location

indeed = "https://www.indeed.co.uk/jobs?q=" + query + "&l=" + location #indeed.co.uk search with type of job and location
reed = "https://www.reed.co.uk/jobs/" + query + "-jobs-in-" + location #reed.co.uk search with type of job and location

response_indeed, response_reed = requests.get(indeed), requests.get(reed) #making a connection to the web pages

soup_indeed, soup_reed = BeautifulSoup(response_indeed.text, "html.parser"), BeautifulSoup(response_reed.text, "html.parser")  #gets the html code from the web pages

#gets data from indeed
indeed_title_div = soup_indeed.find_all("div", {"class" : "title"}) #gets the divs that keep the title of the job
indeed_location = soup_indeed.find_all("span", { "class" : "location accessible-contrast-color-location" }) #gets the spans that keep the location of the job

#gets data from reed
reed_title = soup_reed.find_all("a", { "class": "gtmJobTitleClickResponsive"}) #gets all the titles of the first page jobs
reed_location = soup_reed.find_all("li", {"class": "location"}) #gets all locations of the first page jobs

print("-------------------INDEED JOBS---------------------------")

job_title = [] #keep indeed jobs titles
job_location = [] #keeps indeed job locations

#gets all titles and stores them
for div in indeed_title_div:
    titles = div.find_all("a")
    for title in titles:
        job_title.append(title.text)
        
#gets all the location and stores them
for span in indeed_location:
    job_location.append(span.text)
   
#puts the job titles and job locations together 
indeed_jobs = dict(zip(job_title, job_location))

#prints all indeed jobs
for key in indeed_jobs:
    print(key + "\n" + indeed_jobs[key])

print("-------------------REED JOBS---------------------------")

reed_job_title = [] #keeps reed job titles
reed_job_location = [] #keeps reed job locations

#gets all the titles and stores them
for title in reed_title:
	reed_job_title.append(title.text)

#removes empty titles
for i in reed_job_title:
	if(i == ''):
		reed_job_title.remove(i)

line = 1 #counts jobs

#gets the location of all the jobs except the promoted 
for location in reed_location:
	if(line > 2):
		reed_job_location.append(location.text)
	line += 1

#unites job titles and job locations
reed_jobs = dict(zip(reed_job_title, reed_job_location))

#prints all reed jobs
for key in reed_jobs:
	print(key + reed_jobs[key])