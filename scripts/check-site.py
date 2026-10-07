"""Release checks for routes, accessible controls, metadata and public packaging."""
from pathlib import Path
from html.parser import HTMLParser
import json,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.canonical=0
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in d:self.ids.append(d['id'])
  if tag=='link' and d.get('rel')=='canonical':self.canonical+=1
  if tag=='img':assert d.get('alt') is not None,'Missing alt'
  for key in ['src','href','data-image','data-src']:
   if d.get(key,'').startswith('/') and not d[key].startswith('//'):self.refs.append(d[key])
routes=[x.text.removeprefix('https://home.onegame.tw') for x in ET.parse(r/'sitemap.xml').getroot().iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
for route in routes:
 p=r/route.strip('/')/'index.html';s=p.read_text();h=Page();h.feed(s)
 assert h.h1==1,(route,h.h1)
 assert h.canonical==1,route
 assert len(h.ids)==len(set(h.ids)),route+' duplicated IDs'
 assert all(t not in s for t in ['無人化帝國','三年奇蹟','100% AI','105家店']),route
 for ref in h.refs:
  path=ref.split('#')[0].split('?')[0];f=r/path.lstrip('/')
  if path.endswith('/'):f=f/'index.html'
  assert f.exists(),(route,ref)
for old,target in json.loads((r/'data/redirects.json').read_text()).items():
 p=r/old.strip('/')
 if old.endswith('/') or not p.suffix:p=p/'index.html'
 s=p.read_text();assert '0;url='+target in s;assert 'noindex,follow' in s
assert 'data-story' not in (r/'franchise/system/index.html').read_text(),'Consumer story still in B2B'
assert (r/'index.html').read_text().find('300,000') < (r/'index.html').read_text().find('想找地方玩？')
print('PASS:',len(routes),'pages, metadata, unique IDs, local assets, legacy redirects, B2B separation')
