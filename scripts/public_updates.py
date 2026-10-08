"""Public, customer-safe selections from Ken's approved consultation deck."""
def apply(g):
    globals().update(g)
    def update(route, body):
        title, desc, _ = P[route]
        P[route] = (title, desc, body)
    def before_close(route, content):
        body = P[route][2]
        marker = '<section class="section closing-section">'
        if marker not in body:
            marker = '<section class="section "><div class="wrap"><div class="closing">'
        assert marker in body, route
        update(route, body.replace(marker, content + marker, 1))

    # Keep the homepage short; details belong to the corresponding subject page.
    body = P['/'][2].replace('<h3>品牌、系統、設備，一起規劃。</h3>', '<h3>14 家直營店的經驗，帶進每一次開店。</h3>')
    update('/', body)

    equipment = section('<div class="section-head"><h2>設備跟著訂單走。</h2><p>把開關、密碼與提醒，<br>接進每一次使用流程。</p></div><div class="upgrade-rows"><article><span>分區控電</span><h3>時間到了，留燈讓客人收拾。</h3><p>包廂訂單結束，先關閉冷氣與麻將桌電源，天花板燈再保留 10 分鐘。開放區可將多桌對應同一台冷氣，該區所有桌位都沒有使用中的訂單時才關閉，減少無人區域持續運轉。</p></article><article><span>智能藍牙喇叭與門鎖</span><h3>一筆訂單，一組使用密碼。</h3><p>顧客從訂單取得門鎖與藍牙配對密碼，訂單結束後自動更換。喇叭也能定時或配合訂單廣播，提醒使用時間與店內規範。</p></article><article><span>紅外線冷氣控制</span><h3>自動設定，後台也能一鍵恢復。</h3><p>訂單開始，自動套用預設的制冷或制熱模式與溫度。客人調亂設定時，管理員可從後台一鍵恢復。</p></article></div><p class="caption">依設備配置與系統設定提供，冷氣需先確認機型相容性；實際硬體故障仍需維修。</p>', 'soft', 'equipment')
    operations = section('<div class="split"><div><h2>無人自助，<br>仍然有人管理。</h2><p>從直營店每天遇到的問題，整理出可執行的店務流程。</p></div><div>'+faq([
        ('如何掌握桌況與清潔？', '後台可查看使用中、空閒、待打掃與下一筆訂單時間，搭配清潔任務安排人員。系統協助分工，現場仍需定期清潔與巡檢。'),
        ('客人想換位、改時間或取消？', '管理者可依訂單狀態更換位置、延長或縮短時間。取消期限、次數與退款比例可由店家設定，顧客依訂單與門市公告操作。'),
        ('客服如何接上現場？', '加購 AI 電話後，可串接後台查詢座位與計費方式。需要人員處理的狀況，再透過工單或轉接交接，讓接手人員先了解門市與問題。'),
        ('有哪些可直接使用的營運素材？', '提供已設計的設備排解、常見問答與續時活動等海報，協助現場說明與顧客自助操作；適用內容依店內設備與活動確認。')
    ])+'</div></div>', id='daily-operations')
    loyalty = section('<div class="split"><h2>讓第一次來，<br>有機會變成下一次。</h2><div><p>優惠券、電子時數票券、儲值與會員等級，可依門市設定規劃活動。</p><p>首次消費及邀請分享活動，可依條件自動贈送優惠券或電子票券給符合資格的會員。</p><p class="caption">優惠適用範圍、使用門檻與贈送對象，依各店活動規則設定。</p>'+link('/franchise/#addons','看系統方案與加購服務')+'</div></div>', 'soft', 'member-activities')
    body = P['/franchise/system/'][2]
    body = body.replace(section(addons), equipment + operations + loyalty)
    body = body.replace('使用時段自動通電，結束後斷電。', '依訂單連動設備，結束後分區斷電並保留收拾照明。')
    update('/franchise/system/', body)

    build_support = section('<div class="split"><div><h2>從格局到施工，<br>一起把現場接好。</h2><p>公司可提供硬體裝修與軟裝的一條龍服務，依物件與預算確認交付範圍。</p></div><div><h3>硬體裝修</h3><p>大門、隔間、配電、天花板、地板、冷氣、壁紙與監視器。</p><h3>軟裝設備</h3><p>麻將桌、麻將椅與沙發，配合包廂或開放桌配置。</p><p class="caption">隔間、配電與麻將桌須使用公司指定廠商。裝修、家具與工程另行報價，不含在 30 萬加盟方案內。</p>'+link('/spaces/','看實際門市空間')+'</div></div>', 'soft', 'build-support')
    location = section('<div class="section-head"><h2>有物件，先評估。<br>找場地，也能交給我們。</h2><p>先確認能放幾桌、租金與場地條件，<br>再決定是否往下走。</p></div><div class="split"><div><h3>已有物件：免費桌數初評</h3><p>提供地址、簡單尺寸與現場影片，團隊先評估可配置的包廂與開放桌數。桌數足夠，再確認用途、格局與整體成本。</p><p class="caption">無法陪同每次看房；初評以提供資料為基礎，正式配置仍需現場確認。</p></div><div><h3>還在找店：委託場地開發</h3><p>依約定區域、坪數與租金範圍尋找物件，協助屋主溝通、建築師初步評估與安排看屋。</p><p>委託期一年，最多提供 3 個符合約定需求的物件。屬另行簽約的付費服務，訂金、成交費用及退款條件於委託前說明。</p>'+link(LINE,'詢問場地評估與代找服務','button secondary')+'</div></div>', id='site-support')
    consultation = section('<div class="split"><div><h2>先算清楚，<br>再決定怎麼開。</h2><p>開店評估與營運諮詢 <strong>NT$10,000</strong></p><p>一起討論選址與格局、法規查核項目、建置成本、來客量情境與日常營運。</p></div><div><h3>諮詢費可折抵加盟方案</h3><p>30 萬元方案扣除已付的 1 萬元諮詢費，後續支付 29 萬元。方案包含首次場勘與格局圖；第二次起場勘加畫圖，每次差旅費 1 萬元。</p><p>選址不只比較租金，也看商圈能帶來多少需求。實際投入與回收時間，需要依物件、成本與來客情境評估。</p>'+link(LINE,'預約開店諮詢','button')+'</div></div>', 'soft', 'consultation')
    addons_public = section('<h2>依營運需求，<br>選擇加購服務。</h2><div class="fee-table"><dl><div><dt>AI 電話客服</dt><dd>NT$2,000／月。串接後台查座位、計費方式與常見問題。</dd></div><div><dt>AI 官方 LINE</dt><dd>NT$3,000／月。開通範圍與回覆內容於導入時確認。</dd></div><div><dt>12 小時真人客服</dt><dd>同時加購上述兩項 AI 服務後，可另加 NT$2,000／月。實際服務時段與範圍於合作時確認。</dd></div><div><dt>紙鈔找零升級</dt><dd>一次性 NT$30,000，可找回百元紙鈔，減少補硬幣與銀行換零錢的工作。補款及收款頻率仍依使用量安排。</dd></div></dl></div><p class="caption">加購費用不含在每月 NT$8,000 系統費內；冷氣控制、電子發票及其他設備另依配置報價。</p>'+link('/franchise/system/#equipment','看設備連動與營運功能'), id='addons')
    body = P['/franchise/'][2].replace(section(addons,id='addons'), addons_public)
    update('/franchise/',body)
    before_close('/franchise/', build_support + location + consultation)

    planning = section('<div class="split"><div><h2>包廂或開放桌，<br>依空間與客群安排。</h2><p>包廂重視隱私與休憩空間；開放桌減少隔間，需一起考量鄰桌干擾與共用動線。</p></div><div><h3>常見配置參考</h3><p>包廂約 270 × 330 公分，可配置沙發。開放桌約 240 × 240 公分，共用走道另計。</p><p class="caption">以上為配置經驗，並非法定最低尺寸。桌椅、門片、消防與逃生需求須依實際物件確認。</p>'+link('/franchise/#site-support','提供物件，評估配置方向','button secondary')+'</div></div>', 'soft', 'planning')
    before_close('/spaces/', planning)
