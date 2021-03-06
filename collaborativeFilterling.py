from __future__ import absolute_import
from __future__ import unicode_literals

# jaccard係数を計算
def jaccard(e1, e2):
    set_e1 = set(e1)
    set_e2 = set(e2)
    return float (len(set_e1 & set_e2)) / float(len(set_e1 | set_e2))
# memo
# cos類似度を使うと要素の大きさも見るんだなぁ（今回の実装は要素の大きさを1としている
def cos(e1, e2):
    len1 = float(len(e1))
    len2 = float(len(e2))
    dotProduct = 0.0
    for val1 in e1:
        for val2 in e2:
            if val1 == val2:
                dotProduct = dotProduct + 1.0
    return dotProduct / (len1 * len2)

# key名を取得
def get_key(k):
    return 'jaccard:product:{}'.format(k)

product_x = [1, 3, 5]
product_a = [2, 4, 5]
product_b = [1, 2, 3]
product_c = [2, 3, 4, 7]
product_d = [3]
product_e = [4, 6, 7]

products = {
    'X': product_x,
    'A': product_a,
    'B': product_b,
    'C': product_c,
    'D': product_d,
    'E': product_e,
}

# redis
import redis

r = redis.Redis(host='localhost', port=6379, db=10)

for key in products:
    base_customers = products[key]
    for key2 in products:
        if key == key2:
            continue
        target_customers = products[key2]
        j = cos(base_customers, target_customers)
        r.zadd(get_key(key), key2, j)

print (r.zrevrange(get_key('X'), 0, 2))
print (r.zrevrange(get_key('E'), 0, 2))
