####
# videoid를 주소에서 가져와서 생기는 문제
# 1. 쇼츠 안됨.(https://www.youtube.com/shorts/zhy6ffwq_fg, v= 이 없음)
# 2. v= ... 후 이상한게 더 있는경우(https://www.youtube.com/watch?v=pIQmxUk_FdI&t=26s, v=pIQmxUk_FdI&t=26s &t=26 이부분시간초가있는 url )
# 이 문제는 url을 새롤고침하면 해결됨
# 셀레니움이나 다른걸로 videoid 태그를 크롤링하면 되겠지만 그만금 걸리는 시간이 늘어남
# api문제
# 1. 할당량 하루 최대10000,댓글 100개 가져오는데에 1번 사용됨
#  1만개 댓글을 크롤링한다 했을떄 100번의 요청이 생김, 한도가 10000이니 1만개를 100번 불러오면 끝 10만개면 10번 100만개면 1번이 끝
# 2.트래픽
# 내가 생각할 문제는 아님
####

from fastapi import APIRouter, HTTPException
from googleapiclient.discovery import build
import random
import os
loot = r'C:\fast-api\projects\myapi\domain\youtube\api_key.txt'
with open(loot, 'r') as f:
    api_key = f.read().strip() 
    
# 환경 변수 설정
os.environ['MY_API_KEY'] = api_key

router = APIRouter(
    prefix="/youtube/question",
)

# api_key = 'AIzaSyDJ13uTSxzjNfHwVmN-JXKXWNYUlvyODBg'
youtube_api_service_name = 'youtube'
youtube_api_version = 'v3'

@router.get("/api_answer")
def grab(_url: str):
    try:
        video_id = _url.split('v=')[-1]
        
        api_obj = build(youtube_api_service_name, youtube_api_version, developerKey=api_key)
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()

        comments = []
        for item in response.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([
                comment['authorDisplayName'],  # author
                comment['textDisplay']         # text
            ])

        if 'nextPageToken' in response:
            response = api_obj.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,         
                pageToken=response['nextPageToken'],
                maxResults=100
            ).execute()

        rand = random.randint(0, len(comments) - 1)
        selected_comment = comments[rand]

        return selected_comment

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
