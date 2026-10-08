"""Photo-led ONE experience. Uses only reviewed actual product imagery."""
def apply(g):
 globals().update(g)
 def media(src,caption,kind='phone'):
  return f'<button class="experience-media {kind}" data-image="{src}" data-caption="{caption}" aria-label="放大{caption}"><img src="{src}" alt="{caption}" loading="lazy"><span>{caption} <b>放大 ↗</b></span></button>'
 def story(key,items,compact=False):
  return f'<div class="experience {"compact" if compact else ""}" data-experience><div class="experience-steps">'+''.join(f'<article id="{key}-step-{i}" class="experience-step"><button class="experience-select" aria-controls="{key}-visual-{i}" aria-pressed="{str(i==0).lower()}" data-experience-step="{i}"><span class="step-index">{i+1:02d}</span><h3>{title}</h3><p>{desc}</p></button></article>' for i,(title,desc,src,cap,kind) in enumerate(items))+'</div><div class="experience-stage"><div class="experience-progress" aria-label="切換畫面">'+''.join(f'<button data-experience-nav="{i}" aria-label="{title}" aria-pressed="{str(i==0).lower()}">{i+1:02d}</button>' for i,(title,*_) in enumerate(items))+'</div>'+''.join(f'<div id="{key}-visual-{i}" class="experience-panel" {"hidden" if i else ""}>'+media(src,cap,kind)+'</div>' for i,(title,desc,src,cap,kind) in enumerate(items))+'</div></div>'
 consumer=[('找一間喜歡的店','選地點，看門市。','/assets/one-stores-20261007.png','ONE APP・門市列表','phone'),('選座位與時間','先看空間，再選相聚的時間。','/assets/one-booking-20261007.png','ONE APP・座位預約','phone'),('確認費用，再付款','門市、時段與金額，付款前看清楚。','/assets/one-checkout-20261007.png','ONE APP・結帳畫面','phone'),('到店，開始相聚','依訂單與現場指引使用包廂。','/images/one-yizhong-room.jpg','台中一中店・真實包廂','room')]
 home=P['/'];body=home[2]
 body=body.replace('<div class="hero-image"><img', '<div class="hero-image"><video class="hero-film" muted loop playsinline preload="none" poster="/images/one-yizhong-room.jpg" aria-label="土城亞東店實景短片：包廂、推門與飲品" data-hero-film data-src="/assets/video/one-real-spaces.mp4"></video><button class="film-toggle" data-film-toggle aria-pressed="false">播放門市短片</button><img')
 body=body.replace('留一點時間，給相聚。','留一點時間，給相聚。')
 body=body.replace(section('<h2>第一次來？30 秒看懂。</h2>'+steps(),'soft')+section(appstory()),section('<div class="section-head"><h2>第一次來？<br>30 秒看懂。</h2>'+link('/app/','探索 ONE APP')+'</div>'+story('home',consumer,True),'product-section'))
 # Each detailed subject lives on its own page. Homepage keeps a concise support entry.
 body=body.replace(section(support()),section('<div class="service-entry"><h2>需要幫忙？</h2><p>預約、付款或現場設備，找到對的協助。</p>'+link('/support/','查看客服與常見問題','button secondary')+'</div>'))
 start=body.find('<section class="section "><div class="wrap"><div class="split"><div><h2>顧客用得順，')
 if start!=-1:
  end=body.find('<section',start+8);body=body[:start]+body[end:]
 P['/']=('ONE桌遊｜24H 自助桌遊・麻將｜找門市、看座位、立即預約',home[1],body)
 appitems=[consumer[0],('兩個月內，提早安排','聚會先約好，座位先安排。','/assets/one-booking-20261007.png','ONE APP・預約日期與座位','detail calendar-detail'),('座位與包廂，直接看','空間、時段與方案放在同一頁。','/assets/one-booking-20261007.png','ONE APP・門市座位與方案','phone'),consumer[2],('儲值與會員權益','在門市頁查看餘額與儲值入口；適用範圍依各店規則。','/assets/one-booking-20261007.png','ONE APP・門市儲值與會員入口','detail member-detail')]
 P['/app/']=(P['/app/'][0],P['/app/'][1],section('<div class="app-intro"><div><p class="eyebrow">ONE APP</p><h1>相聚的事，<br>在手機上安排。</h1><p>找門市。選座位。留一段好時光。</p>'+link(BOOK,'開啟 ONE APP','button')+'</div>'+media('/assets/one-booking-20261007.png','ONE APP・真實預約畫面')+'</div>','app-hero')+section(story('app',appitems),'app-product')+section('<div class="split"><h2>訂單在手，<br>時間自己安排。</h2><div><p>回到訂單查看預約。還想繼續？先確認後續空檔與續時費用。</p>'+link(BOOK,'開啟我的 ONE','button')+'</div></div>','soft')+finalcta())
 # A real system clip, explicitly distinguished from a customer call recording.
 audio=section('<div class="audio-proof"><div><p class="eyebrow">AI 電話・實際系統音檔</p><h2>先聽聽，<br>電話如何被接起。</h2><p>來自 ONE 語音系統的接聽開場音檔。</p></div><div><audio controls preload="none" aria-label="播放 ONE AI 電話接聽開場"><source src="/assets/audio/one-phone-greeting.mp3" type="audio/mpeg">你的瀏覽器不支援音訊播放。</audio><details><summary>查看逐字稿</summary><blockquote>你好，我是萬桌遊 AI 語音助理，本通電話將錄音，可以直接跟我說你的需求。</blockquote></details><p class="caption">這段是系統預錄開場，不是顧客通話錄音或即時查位示範。ONE 在音檔中以「萬」發音。</p></div></div>','soft')
 p=P['/support/'];P['/support/']=(p[0],p[1],p[2].replace(section(support()),audio+section(support())))
 # How-to is a short practical checklist, not another product walkthrough.
 p=P['/how-it-works/'];P['/how-it-works/']=(p[0],p[1],p[2].replace(section(appstory(),'soft'),section('<div class="split"><h2>畫面怎麼操作？</h2><div><p>用實際 APP 畫面，跟著看一次。</p>'+link('/app/','看 ONE APP 操作','button secondary')+'</div></div>','soft')))
 def scene(name,caption,cl=''):
  return '<figure class="scene '+cl+'">'+media('/images/'+name+'.jpg',caption,'room')+'</figure>'
 spacebody=section('<div class="spaces-title"><p class="eyebrow">ONE SPACES</p><h1>留一個空間，<br>給相聚。</h1><p>不同城市，不同樣子。都是實際的 ONE。</p></div>','intro')
 spacebody+=section(scene('one-yizhong-entrance','台中一中店・入口實景','scene-wide'),'photo-section')
 spacebody+=section(scene('one-fuda-lounge','新莊輔大店・沙發包廂','scene-wide'),'photo-section')
 spacebody+=section('<div class="section-head"><h2>挑一個，<br>喜歡的角落。</h2><p>座椅、色彩與光線，<br>每間店都有自己的性格。</p></div><div class="scene-trio">'+scene('one-guangcai-room','嘉義光彩店・暖橘座椅')+scene('one-yadong-green','土城亞東店・綠色包廂')+scene('one-yadong-yellow','土城亞東店・明亮包廂')+'</div>','photo-section')
 spacebody+=section('<div class="section-head"><h2>再多看一點。</h2><div class="gallery-controls"><button data-gallery-prev aria-label="上一張門市照片">←</button><button data-gallery-next aria-label="下一張門市照片">→</button></div></div>'+gallery(),'spaces-section')+section('<div class="closing"><h2>找到喜歡的空間，<br>就出發。</h2>'+link('/find/','查看各店座位與價格','button')+'</div>')
 P['/spaces/']=(P['/spaces/'][0],P['/spaces/'][1],spacebody)
 business=[('一間真實的 ONE','從場地、格局，到顧客走進門。','/images/one-yizhong-entrance.jpg','台中一中店・實際門市','room'),('用 APP 接住預約','顧客選座位、付款，建立訂單。','/assets/one-booking-20261007.png','ONE APP・顧客預約','phone'),('後台掌握全店','桌況、訂單與營收，集中查看。','/assets/one-admin-20261007.png','ONE 店家後台・營運總覽','phone'),('自助收款，接上現場','現金與 LINE Pay，依門市設備指引操作。','/images/one-guangcai-kiosk.jpg','嘉義光彩店・自助繳費機','room')]
 p=P['/franchise/'];intro_end=p[2].find('<section class="section "><div class="wrap"><div class="split"><h2>加入的，')
 if intro_end!=-1:
  end=p[2].find('<section',intro_end+8)
  body=p[2][:intro_end]+section('<h2>加入 ONE，<br>你得到什麼？</h2>'+story('business',business),'business-product')+p[2][end:]
  P['/franchise/']=(p[0],p[1],body)
 p=P['/franchise/system/'];P['/franchise/system/']=(p[0],p[1],p[2].replace(section(appstory(),'soft'),section('<div class="operations-flow"><h2>一筆訂單，<br>接好門店日常。</h2><ol>'+''.join(f'<li><span>{i:02d}</span><h3>{a}</h3><p>{b}</p></li>' for i,(a,b) in enumerate([('顧客預約','在 ONE APP 選座位與時間。'),('付款與訂單','確認付款後，依訂單使用時段安排。'),('現場控電','使用時段自動通電，結束後斷電。'),('現場自助收款','繳費機支援現金與 LINE Pay。'),('桌況與營收','後台集中查看營運資訊。'),('客服接手','依門市開通情況提供 AI 電話與人員協助。')],1))+'</ol></div>','soft')))
 return story
