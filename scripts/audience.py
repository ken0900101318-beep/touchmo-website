"""Franchise-first entry, with consumer and merchant downloads kept distinct."""
def apply(g):
 globals().update(g)
 import re
 home=P['/'];parts=re.findall(r'<section\b.*?</section>',home[2],re.S)
 hero=parts[0].replace('24H 自助桌遊・麻將空間','ONE 品牌加盟・自助休閒空間').replace('想玩，<br>就來。','想開店，<br><span class="hero-line">從 ONE 開始。</span>').replace('從找門市、選座位到預約付款，<br>用 ONE APP 就能完成。','從場地規劃、系統到現場設備，<br>接上 ONE 的品牌與營運經驗。')
 hero=hero.replace(link('/find/','找附近門市','button'),link('/franchise/','了解加盟方案','button')).replace(link(BOOK,'立即預約','button secondary'),link('/franchise/system/','看營運系統','button secondary')).replace(link('/franchise/','了解加盟 ONE'),link('https://store.onegame.tw/dl/','下載店家管理 APP ↗'))
 overview=section('<div class="section-head"><h2>開一間店，<br>也接上一套營運方式。</h2><p>顧客用 APP 預約，<br>店家用後台掌握日常。</p></div><div class="franchise-overview"><div>'+shot('one-admin-20261007.png','ONE 店家後台・營運總覽')+'</div><div><h3>品牌、系統、設備，一起規劃。</h3><p>ONE APP、店家後台、智慧控電與自助繳費，接上同一筆訂單。</p><p class="home-price">NT$ <strong>300,000</strong></p><p>含 10 組控電、1 台繳費機，場勘與格局設計各 1 次。</p>'+link('/franchise/#pricing','看方案內容與其他費用','button')+'<p class="caption">超出組數、施工與加購另計，依正式報價確認。</p>'+link('/franchise/system/','看實際營運流程')+'</div></div>','soft')
 space=section('<div class="section-head"><h2>真正開起來的 ONE。</h2>'+link('/spaces/','看看各店空間')+'</div>'+gallery(),'spaces-section')
 start=section('<div class="closing"><h2>先聊地點，<br>再一起算清楚。</h2><div>'+link(LINE,'諮詢加盟','button')+link('tel:0809099006','免付費 0809-099-006')+'</div></div>','closing-section')
 consumer=section('<div class="section-head"><h2>想找地方玩？</h2><p>選門市、看座位，再出發。</p></div>'+finder()+ '<div class="actions">'+link('/app/','看看顧客 APP')+link('/download/#customer','下載 ONE聚 APP')+link('/how-it-works/','第一次來怎麼玩')+'</div>',id='find')
 P['/']=('ONE桌遊｜品牌加盟・智慧營運系統・開店方案','想開一間 ONE？了解品牌加盟、30 萬方案、APP 與店家後台、控電及自助設備，也能查找全台門市。',hero+proof()+overview+space+start+consumer)
 ios='https://apps.apple.com/tw/app/id6469089066';android='https://play.google.com/store/apps/details?id=one.zhuoyou'
 downloads=section('<div class="download-grid"><article id="merchant"><p class="eyebrow">給店家</p><h2>ONE 店家管理</h2><p>管理門市、訂單、桌況與營收。<br>下載頁會依手機顯示適合的版本。</p>'+link('https://store.onegame.tw/dl/','下載店家管理 APP','button')+'<p class="caption">已有店家帳號的管理者使用。</p>'+link('https://store.onegame.tw/#/','開啟店家網頁版 ↗')+'</article><article id="customer"><p class="eyebrow">給顧客</p><h2>ONE聚</h2><p>找門市、選座位、預約與付款。<br>在商店搜尋「ONE聚」。</p><a class="button" href="'+android+'" data-customer-download hidden>下載 ONE聚 APP</a><div class="download-options">'+link(ios,'iPhone／iPad・App Store ↗')+link(android,'Android・Google Play ↗')+'</div>'+link(BOOK,'先使用網頁版預約 ↗')+'</article></div>','download-section')
 P['/download/']=('APP 下載｜ONE桌遊・店家管理與 ONE聚','店家管理 APP 與顧客 ONE聚下載入口，依 iPhone、iPad 或 Android 顯示適合的商店連結。',intro('用對的 APP，<br>開始你的 ONE。','經營門市與預約座位，各有專屬入口。')+downloads)
 p=P['/app/'];P['/app/']=(p[0],p[1],p[2].replace(link(BOOK,'開啟 ONE APP','button'),link('/download/#customer','下載 ONE聚 APP','button')+' '+link(BOOK,'開啟網頁版')))
 p=P['/franchise/system/'];P['/franchise/system/']=(p[0],p[1],p[2].replace('ONE APP × 店家後台 × 現場設備</p>','ONE APP × 店家後台 × 現場設備</p><div class="actions">'+link('https://store.onegame.tw/dl/','下載店家管理 APP','button secondary')+'</div>'))
 nav[:]=[('/franchise/','加盟方案'),('/franchise/system/','營運系統'),('/spaces/','門市空間'),('/download/','APP 下載'),('/about/','品牌故事'),('/find/','找門市')]
