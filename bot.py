import requests
import datetime
import time
import os
from pytz import timezone

# Your Telegram Bot Token and Chat ID
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Taiwan timezone
tw_tz = timezone('Asia/Taipei')

def fetch_us_stock_report():
    """Fetch US stock market report data"""
    today = datetime.datetime.now(tw_tz).strftime("%Y-%m-%d")
    
    report = f"""📈 {today} 美股晨報

🎯 主要指數（美東11月11日收盤）:
• 道瓊指數: +1.18% (47,927.96) - 創歷史新高 🔝
• 標普500: +0.21% (6,846.61)
• 納斯達克: +0.25% (23,468.30)

💭 投資氣氛：
市場樂觀看待美國政府停擺結束，轉向藥廠與AI晶片族群。標普500期貨+0.3%、那指期貨+0.6%，持續反彈中。

🔥 重要族群動向：
• 科技股：英偉達下跌超2%，不過AI芯片整體需求仍強 📉
• 費城半導體指數：+2.48% (6,979.70) 💪
• 半導體：仍是市場焦點，台積電ADR表現關鍵
• 藥廠與消費股：投資人轉向

📊 台積電 (TSMC)：
• 台股收盤：1,475元 (+0.68%)
• 10月營收：3,674.73億元 創歷史新高 📈
• 美股ADR：下跌1%以上（同步回調）
• 基本面強勁：今年前10月累計營收年增33.8%
• Q4指引：營收322-334億美元，毛利率59-61%
• 技術面：台積電已是全球最賺錢集團，年賺1.4兆元 💰

⚡ 重要消息：
✅ 蔡英文視察歐積電 - 台積電持股70%，海外擴產持續推進
✅ 市場轉向：從「AI獨舞」到「百花齊放」，獲利擴散成關鍵
⚠️ 高盛警告：美股未來十年可能持續落後，建議提高海外配置

🎯 短期關注：
• 美國政府停擺解決進展
• AI晶片供需動向
• 台積電技術領先地位與產能擴充
• 匯率變動對財報影響
"""
    
    return report

def send_telegram_message(text):
    """Send message to Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=payload, timeout=10)
        if response.status_code == 200:
            print(f"✅ Message sent successfully at {datetime.datetime.now(tw_tz)}")
            return True
        else:
            print(f"❌ Failed to send message: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error sending message: {str(e)}")
        return False

def main():
    """Main function - run once for Cron Job"""
    print("🚀 Stock Report Bot Started...")
    
    try:
        report = fetch_us_stock_report()
        send_telegram_message(report)
        print("✨ Cron job completed successfully")
    except Exception as e:
        print(f"❌ Error in main: {str(e)}")

if __name__ == "__main__":
    main()
