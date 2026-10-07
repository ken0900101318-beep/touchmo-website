"""Publish only current HTML and assets; retain archived source in Git, not on the site."""
from pathlib import Path
import shutil,sys,json,re,xml.etree.ElementTree as ET
r=Path(__file__).resolve().parents[1];out=Path(sys.argv[1]).resolve()
if out.exists():raise SystemExit('Use a new output directory; do not erase existing files.')
out.mkdir(parents=True)
files={'index.html','404.html','robots.txt','sitemap.xml','CNAME','one-logo.jpg','.nojekyll'}
for loc in ET.parse(r/'sitemap.xml').getroot().iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
 path=loc.text.removeprefix('https://home.onegame.tw').strip('/')
 files.add((path+'/' if path else '')+'index.html')
for old in json.loads((r/'data/redirects.json').read_text()):
 path=old.strip('/');files.add(path+'/index.html' if old.endswith('/') or not Path(path).suffix else path)
files.update(['assets/one.css','assets/one.js'])
for name in list(files):
 if name.endswith('.html'):
  for asset in re.findall(r'(?:src|data-src|data-image)="(/(?:assets|images)/[^"?]+)',(r/name).read_text()):files.add(asset.lstrip('/'))
files.update('data/'+x for x in ['stores.json','brand-stats.json','space-photos.json'])
for name in sorted(files):
 target=out/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(r/name,target)
print('Packaged',len(files),'approved public files. Historical Markdown/source excluded.')
