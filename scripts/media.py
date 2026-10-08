"""Responsive public previews; full-resolution originals load only on demand."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def optimize(body):
    manifest=json.loads((R/'data/media-variants.json').read_text())
    first=True
    def image(m):
        nonlocal first
        tag=m.group(0);src=re.search(r'src="([^"]+)"',tag)
        if not src or src[1] not in manifest:return tag
        media=manifest[src[1]];variants=media['variants'];small=variants[0]['src']
        sizes='(max-width: 760px) 90vw, 660px'
        if 'one-admin' in src[1] or 'one-booking' in src[1] or 'one-checkout' in src[1] or 'one-stores' in src[1]:sizes='(max-width: 760px) 90vw, 420px'
        eager='fetchpriority="high"' in tag or first
        first=False
        tag=re.sub(r'\s(?:src|width|height|loading)="[^"]*"','',tag)
        srcset=', '.join(f'{v["src"]} {v["width"]}w' for v in variants)
        attrs=f' width="{media["width"]}" height="{media["height"]}" decoding="async" sizes="{sizes}"'
        if eager:attrs+=f' srcset="{srcset}" src="{small}" loading="eager"'
        else:attrs+=f' data-deferred-src="{small}" data-deferred-srcset="{srcset}" loading="lazy"'
        return tag[:-1]+attrs+'>'
    body=re.sub(r'<img\b[^>]*>',image,body)
    # The hero image is already visible. Avoid fetching a second JPEG for the video poster.
    body=body.replace('poster="/images/one-yizhong-room.jpg"','').replace('data-src="/assets/video/one-real-spaces.mp4"','data-src="/assets/video/one-real-spaces-lite.mp4"')
    return body
