from matplotlib import pyplot as plt
import numpy as np

# 输入数据
full_board = {"mid_price": 35625,
              "bids": [{"price": 35000, "size": 3}, {"price": 34000, "size": 2}, {"price": 33000, "size": 1}, ],
              "asks": [{"price": 38000, "size": 6}, {"price": 37000, "size": 5}, {"price": 36000, "size": 4}, ]}


ask_size_list = [item["size"] for item in full_board["asks"]]
ask_price_list = [item["price"] / 1000 for item in full_board["asks"]]

bid_size_list = [item["size"] * -1 for item in full_board["bids"]]
bid_price_list = [item["price"] / 1000 for item in full_board["bids"]]


plt.barh(bid_price_list, bid_size_list, align='center', alpha=0.4, color='g')
plt.barh(ask_price_list, ask_size_list, align='center', alpha=0.4, color='r')
# plt.ylim([-1, len(X_asks) + 0.1])
# plt.xlim([-max(X_bids) - 1, max(X_asks) + 1])
plt.grid()

plt.show()
