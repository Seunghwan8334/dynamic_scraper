import requests
from bs4 import BeautifulSoup

ALL_JOBS = []

class JOB:
    def __init__(self, skill, name, company, description, link):
        self.skill = skill 
        self.name = name 
        self.company = company 
        self.description = description 
        self.link = link 

response = requests.get("https://berlinstartupjobs.com/engineering/",
    headers={
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

soup = BeautifulSoup(response.content, "html.parser")   

page_number = len(soup.find_all(class_="page-numbers"))-1 #Next 는 뺴줌 

for i in range(1,page_number+1):
    url = "https://berlinstartupjobs.com/engineering/page/"+str(i)+"/"
    response = requests.get(url,
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    jobs = soup.find_all("li",class_="bjs-jlid")
    for job in jobs:
        job.find("h4",class_="bjs-jlid__h")
        name = job.find("h4",class_="bjs-jlid__h").find("a").text 
        company = job.find("a",class_="bjs-jlid__b").text
        description = job.find("div",class_="bjs-jlid__description").text 
        link = job.find("h4",class_="bjs-jlid__h").find("a")["href"]
        ALL_JOBS.append(JOB("engineer",name,company,description,link))





skills = ["python", "typescript", "javascript", "rust"] 

for skill in skills:
    url = "https://berlinstartupjobs.com/skill-areas/"+skill 
    response = requests.get(url,
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

    soup = BeautifulSoup(response.content, "html.parser",)    
    jobs = soup.find_all("li",class_="bjs-jlid")
    for job in jobs:
        job.find("h4",class_="bjs-jlid__h")
        name = job.find("h4",class_="bjs-jlid__h").find("a").text 
        company = job.find("a",class_="bjs-jlid__b").text
        description = job.find("div",class_="bjs-jlid__description").text 
        link = job.find("h4",class_="bjs-jlid__h").find("a")["href"]
        ALL_JOBS.append(JOB(skill,name,company,description,link))
                
#모든 직업을 JOB클래스로 감싼 뒤 ALL_JOBS 리스트에 넣어줬음

