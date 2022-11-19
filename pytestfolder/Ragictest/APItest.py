from distutils.log import info
from email import header
import requests as req
import json

# url="https://ap3.ragic.com/haisann/forms2/5?api=true"
url2='http://haisiannerpsys.org/hsweb/sub_index_web/Consumabels_apply_form.html'


header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
# header={
#     "Authorization":"Basic cEg1bCtoV040TFBzYVA3REs1cGJBUW5mSjUwWm1kOExrRXVWenkzM3R0V0krVGE0UDlkOFpJUXlKSEdsektUUjR2ZXgxV21vSXVjPQ=="
# }

# param={
    
# }

# b='https://ap3.ragic.com/haisann/forms2/5?api=true'
# c='https://ap3.ragic.com/haisann/forms2/1?api=true'


r=req.get(url2,headers=header)
print(r.text)
# pushdata={
#     '1000164':'2022/09/07',
#     '1000135':'2022/09/08 10:00',
#     '1000136':'2022/09/10 10:00',
#     '1000346':'不知道',
#     '1000138':'???',
#     '1000140':'12',
#     '1000141':'chenyouduan@gmail.com',
#     '1000142':'justin',
#     '1000143_-1':'安全飛盤',
#     '1000145_-1':'1',
#     '1000143_-2':'弓箭',
#     '1000145_-2':'1',
# }
# pushdata_json=json.dumps(pushdata)
#  "where":"1000135,gte,2022/09/08",
# filter_parms={
#     "info":"false",
#     "info":"true"
# }



# filter_parms_json=json.dumps(filter_parms)
# r=req.get(url,headers=header,params=filter_parms)
# print(r.text)