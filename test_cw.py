import requests
response = requests.get("https://api.monobank.ua/bank/currency")
print(response)
print(response.status_code)
data = response.json()
rate_usd = data[0]
amount = int(input("enter dollar amount: "))
# print(data)
print(amount * rate_usd["rateBuy"])

# https://the-trivia-api.com/docs/v2/#tag/Questions/operation/getRandomQuestions
# https://jsonplaceholder.typicode.com/