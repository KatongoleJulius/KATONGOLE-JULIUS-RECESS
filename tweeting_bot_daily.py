import tweepy
import schedule
import time

# === 🔐 Twitter API credentials (Paste yours below) ===
API_KEY = "nrYI2k0alMG1KQgtxLr5huBkX"
API_SECRET = "iJqusDnA6kkfWb542vDkVr83bQw9eP6T5az3Vy8XqNjJBjBlGg"
ACCESS_TOKEN = "1600681715441324032-txVtXLNhaYSOEWw9e3VfaVpBtiVJGO"
ACCESS_TOKEN_SECRET = "9BvEDJgVBaIQcrMQ5GIxBwg0Xu8X68bx1G3XbykUxFXhd"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHGP2wEAAAAAAEIcwThpPCuFP9tXqljNwuo9TFI%3DUTCp8CcN2TOTtNw06ogBPxczMxqXBN2Z4ChRCsRvGgqNZ8kIN5"  # Required for tweepy.Client

# === 🧠 Authenticate using Twitter API v2 ===
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# === 🐦 Function to create a tweet ===
def post_tweet():
    tweet = "🌍 Hello world! This is your scheduled daily tweet. #DailyBot"
    try:
        client.create_tweet(text=tweet)
        print("✅ Tweet sent successfully.")
    except Exception as e:
        print("❌ Failed to send tweet:", e)

# === ✅ POST IMMEDIATELY NOW ===
post_tweet()

# === 🕒 Also schedule the tweet daily at 10:00 AM ===
schedule.every().day.at("10:00").do(post_tweet)

print("🟢 Daily Tweet Bot is running... (Ctrl+C to stop)")

# === 🔁 Keep checking for scheduled tasks ===
while True:
    schedule.run_pending()
    time.sleep(60)
