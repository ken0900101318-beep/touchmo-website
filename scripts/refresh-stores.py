"""Read-only public directory import. Never save full API objects."""
import json,urllib.request,datetime,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
def read(path,data=None):
 r=urllib.request.urlopen(urllib.request.Request('https://www.onegame.tw/api/index/'+path,data=data,headers={'User-Agent':'ONE-Website-Directory/1.0'}),timeout=30)
 d=json.load(r)
 if d.get('code')!=1:raise ValueError('Public directory unavailable')
 return d['data']
cities={x['id']:x['name'] for x in read('getCitys')};rows=[]
for x in read('stores',b''):
 if x['id']==76 or any(s in x['name'] for s in ['測試','test','Test']):continue
 rows.append({'id':x['id'],'name':x['name'],'city':cities.get(x['city_id'],''),'address':x['address'],'lat':float(x['lat'] or 0),'lon':float(x['lon'] or 0),'image':x.get('image',''),'hours':f"{x['open']}–{x['close']}" if x['open']!=x['close'] else '營業時間請查看門市','preparing':'籌備' in x['name']})
(root/'data/stores.json').write_text(json.dumps({'updatedAt':datetime.date.today().isoformat(),'stores':rows},ensure_ascii=False,indent=2))
print('Public fields only:',len(rows),'stores')
