import requests
from secret import API_KEY

BASE_URL = (
    "https://www.kobis.or.kr/kobisopenapi/webservice/"
    "rest/boxoffice/searchDailyBoxOfficeList.json"
)


# 첫 번째 함수: 박스오피스 1위 영화 제목
def get_boxoffice_rank_1(date):
    """
    그 날짜의 박스오피스 1위 영화 제목을 알려준다.

    받는 것: date ("20260824") 
    돌려주는 것: ("오디세이") 
    """
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    return movies[0]["movieNm"]