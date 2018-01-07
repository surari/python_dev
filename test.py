from __future__ import absolute_import, unicode_literals

from collections import defaultdict

ITEM_10_BUY_USERS = ['A', 'C', 'E', 'G']
INDEX_BASE = 'INDEX_BUY_HISTORY_USER_{}'
INDEX = {
    'INDEX_BUY_HISTORY_USER_A': [10, 20, 50, 60, 90],
    'INDEX_BUY_HISTORY_USER_B': [20, 20, 50, 60, 70],
    'INDEX_BUY_HISTORY_USER_C': [10, 30, 50, 60, 90],
    'INDEX_BUY_HISTORY_USER_D': [30, 40, 50, 60],
    'INDEX_BUY_HISTORY_USER_E': [10],
    'INDEX_BUY_HISTORY_USER_F': [70, 80, 90],
    'INDEX_BUY_HISTORY_USER_G': [10, 70, 90],
}

result = defaultdict(int)
for user_id in ITEM_10_BUY_USERS:
    buy_history = INDEX.get(INDEX_BASE.format(user_id))
    for item_id in buy_history:
        result[item_id] += 1

l = []
for key in result:
    l.append((key, result[key]))

l.sort(key=lambda x: x[1], reverse True)
print l