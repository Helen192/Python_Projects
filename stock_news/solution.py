import requests
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7dda47a69e1cf63f4d9b99c62e2c475d"
# Your Auth Token from twilio.com/console
auth_token  = "bd93105925ceee4ebaf2241984bc4593"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API key of newsapi.org
NEWS_API_KEY ="94ee2f1b530c4f6792422a47d5f077f8"

#API key of alphavantage.co
STOCK_API_KEY = "AI940Y0HNKUDXEPM"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
# Getting stock data from API alphavantage.co
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between closing price of yesterday and day before yesterday
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

#TODO 5. - If different percentage is greater than 5 then use the News API to get articles related to the COMPANY_NAME
if abs(diff_percent) >= 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]

    #TODO 6. - Use Python slice operator to create a list that contains the first 3 articles
    three_articles = articles[:3]

    #STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number

    #TODO 7. - Create a new list of the first 3 article's headline and description using list comprehension
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    #TODO 8. - Send each article as a separate message via Twilio
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+19108385518",
            to="+4917624679967"
        )





