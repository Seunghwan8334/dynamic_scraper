from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from file import save_to_file

keywords = [
    "flutter",
    "kotlin",
    "nextjs"
]

p = sync_playwright().start() 

browser = p.chromium.launch(headless=False) #크롬 브라우저 런치

page = browser.new_page() #새 페이지

for keyword in keywords:
    page.goto("https://www.wanted.co.kr") #사이트로 이동
    time.sleep(1)
    page.click("button.Aside_searchButton__rajGo") #버튼 클릭
    time.sleep(1)
    page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword) #입력
    time.sleep(1)
    page.keyboard.down("Enter") #엔터 
    time.sleep(1)
    page.click("a#search_tab_position") #클릭
    time.sleep(1)
    for _ in range(5):
        page.keyboard.down("End")
        time.sleep(1) 
    content = page.content()
    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__REty8")
    
    jobs_db = []

    for job in jobs:
        link = job.find("a")["href"]
        link = "https://www.wanted.co.kr"+link
        title = job.find("strong", class_="JobCard_title__HBpZf").text
        company = job.find("span", class_="JobCard_companyContent___EEde").text
        reward = job.find("span", class_="JobCard_reward__cNlG5").text

        job = {
            "title":title,
            "comapny":company,
            "reward":reward,
            "link":link
        }
        jobs_db.append(job)
        save_to_file(keyword, jobs_db)

p.stop()