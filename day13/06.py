'''
在一个字典中保存了股票的代价和价格,找出股价大于100元的股票并
创建一个新的字典
'''

stocks = {
    'aapl':191.88,
    'good':1186.96,
    'ibm':149.24,
    'orcl':48.44,
    'acn':166.89,
    'fb':208.09,
    'symc':21.29
}

stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)