from fastapi import APIRouter

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
import time
import random

from domain.question import question_router
router = APIRouter(
    prefix="/youtube/question",
)


# options = webdriver.ChromeOptions()

# options.add_argument("headless")

# driver = webdriver.Chrome(executable_path="/chromedriver", options=options)


@router.get("/answer")
def grab(_url):
    url = _url
    options = webdriver.ChromeOptions()

    options.add_argument("headless")

    # driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get(url)

    time.sleep(5) 

    for _ in range(10):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1) 

    comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")
    authors = driver.find_elements(By.CSS_SELECTOR, "#author-text")
    
    texts = [comment.text for comment in comments]
    name = [author.text.strip() for author in authors]

    driver.quit()

    rand = random.randint(0, len(texts))
    end_name = name[rand]
    end_texts = texts[rand]
    # print(f'아이디 {len(name)}, 내용 {len(texts)}')
    # print(f'랜덤번호:{rand}')
    # print(f'당첨자 이름: {name[rand]}')
    # print(f'당첨 내용: {texts[rand]}')

    return end_name, end_texts
# #----------------챗지피티가 만든거------------------------------------------
# from fastapi import APIRouter, FastAPI, HTTPException

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import random     

# router = APIRouter(
#     prefix="/youtube/question",
# )

# @router.get("/answer")
# def grab(url: str):
#     options = webdriver.ChromeOptions()
#     options.add_argument("headless")
#     service = ChromeService(executable_path="./chromedriver")
    
#     try:
#         driver = webdriver.Chrome(service=service, options=options)
#         driver.get(url)

#         time.sleep(5) 

#         for _ in range(10):
#             driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#             time.sleep(1)

#         comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")
#         authors = driver.find_elements(By.CSS_SELECTOR, "#author-text")
        
#         texts = [comment.text for comment in comments]
#         names = [author.text.strip() for author in authors]

#         driver.quit()

#         if not texts or not names:
#             raise HTTPException(status_code=404, detail="No comments found")

#         rand = random.randint(0, len(texts) - 1)
#         end_name = names[rand]
#         end_text = texts[rand]

#         print(f'아이디 {len(names)}, 내용 {len(texts)}')
#         print(f'랜덤번호:{rand}')
#         print(f'당첨자 이름: {end_name}')
#         print(f'당첨 내용: {end_text}')

#         return {"name": end_name, "text": end_text}

#     except Exception as e:
#         if driver:
#             driver.quit()
#         raise HTTPException(status_code=500, detail=str(e))

