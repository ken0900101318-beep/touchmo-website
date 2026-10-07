# ONE桌遊官方網站

- 正式網址：https://home.onegame.tw/
- 原始倉庫：https://github.com/ken0900101318-beep/touchmo-website
- 託管：GitHub Pages，main 根目錄，保留 CNAME。
- 產生頁面：`python3 scripts/build.py`；部署來源是產出的 HTML 與 assets。
- 更新真實公開門市名錄：`python3 scripts/refresh-stores.py`（唯讀，只儲存公開展示欄位；不保存完整API回應）。
- 本機預覽：`python3 -m http.server 4320`。
- 實績唯一來源：`data/brand-stats.json`。品牌100+、會員164392、2023開始，統計日期2026-10-06；不是把公開名錄筆數當營運家數。
- 公開數據網址：https://home.onegame.tw/data/brand-stats.json ，可供母品牌後續接入。本轮依Ken指示未修改遊戲家網站，兩站尚非自動同步。
- 消費費率與座位：導向ONE真實門市預約頁；本站不計算或捏造空位／收費。
- 加盟：30萬元，10組控電+1台繳費機等。月費／抽成／交易手續費與加購單價未取得正式數字，頁面明列待正式報價。
- 客服區是情境指引，不是假AI對話；未改ONE後端、付款、AI語音服務。
- 圖片：使用既有ONE官網門店實景、官方Logo，以及Ken提供的真實產品畫面；可點擊放大。
- 原始網站完整備份：`/Users/ken/Downloads/ken-agent/outputs/one-official-before-20261007`，Git歷史亦保留。舊HTML入口轉向新版，未刪檔。
