import requests
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7dda47a69e1cf63f4d9b99c62e2c475d"
# Your Auth Token from twilio.com/console
auth_token  = "bd93105925ceee4ebaf2241984bc4593"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API key of newsapi.org
NEWS_API_KEY ="94ee2f1b530c4f6792422a47d5f077f8"
news_parameters = {
    "q": COMPANY_NAME,
    "qinTitle": "title search",
    "language": "en",
    "apiKey": NEWS_API_KEY
}


#API key of alphavantage.co
ALPHA_API_KEY = "AI940Y0HNKUDXEPM"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_API_KEY
}
# Getting stock data from API alphavantage.co
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = response.json()
daily_stock = list(stock_data["Time Series (Daily)"].items())
#print(stock_data)
#print(daily_stock)
#print(daily_stock[0][1]['1. open'])


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

compared_stock = abs(float(daily_stock[0][1]['4. close']) - float(daily_stock[1][1]['4. close']))
compared_stock_percentage = (compared_stock / float(daily_stock[0][1]['4. close'])) * 100

if compared_stock_percentage >= 1:
    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
    #HINT 1: Think about using the Python Slice Operator
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = response_news.json()
    # get the first three articles from API news sources
    first_three_news_data = news_data["articles"][:3]
    # convert title and description of the first three articles into a list
    list_articles = [(first_three_news_data[x]["title"], first_three_news_data[x]["description"]) for x in range(len(first_three_news_data))]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.
    for article in list_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+4917624679967",
            from_="+19108385518",
            body=f"Headline: {article[0]}\n\nBrief: {article[1]}")

        print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


