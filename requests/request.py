import requests
import json


url = 'https://www.tournmaster.com/seantour_map/travel/getBeachCongestionApi.do'

data = requests.get(url).json()

# data = json.loads(result.text)

# Beach16 - 함덕
# Beach19 - 협재
# Beach23 - 이호테우
# Beach26 - 곽지
# Beach29 - 금능
# Beach34 - 중문
# Beach36 - 김녕

id_list = [16, 19, 23, 26, 29, 34, 36]
ll = [data[f'Beach{id}']['congestion'] for id in id_list]
lll = [data[f'Beach{id}']['poiNm'] for id in id_list]

print(ll)
print(lll)
