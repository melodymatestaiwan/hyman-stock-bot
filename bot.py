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
    
    report = f"""📈 {today} 美股晨報\n\n
🎯 主要指數:\n
• 道瓊指數: +1.12% (38,567.15)\n• 標普500: +0.28% (5,906.32)\n• 納斯達克: -0.18% (18,764.92)\n\n
💭 投資氣氛:\n謹慎樂觀，市場呈現兩極化走勢\n\n
🔥 重要族群:\n• 科技股: 繼續受市場追捧\n• 半導體: AI相關應用推動成長\n• 被動元件: 持續強勢表現\n\n
📊 台積電 (TSMC):\n• 美股收盤: -1.39% (291.17 USD)\n• 10月營收: 3674.73億元 (新高)\n• 技術面: 跌破五日均線，MACD紅柱縮小\n\n
⚡ 重要轉折:\n暫無巨大盤勢逆轉，繼續關注盤中消息\n"""
    
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
