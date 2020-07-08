d = {'key': 'value', 'another_key': 'another_value'}
print(d)

key_list = [1, 2, 3]
value_list = [True, True, False]
d = dict(zip(key_list, value_list))
print(d)

d2 = dict(d)
print(d2)
tuple_d = dict([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
print(tuple_d)

keyword_d = dict(key1='value1', key2='value2', key3='value3')
print(keyword_d)
dict_comprehensions = {x: x * 100 for x in range(10) if x %% 2 == 1}
print(dict_comprehension)

d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
d['3rd Key'] = True
print(d)
d['my_key'] = 'new value'
print(d)

d = dict(key1='value1', key2='value2', key3='value3')
d.update(key4='value4')
print(d)

d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
d['my_key']
# ERROR d['my_missing_key']
print(d.get('my_missing_key'))
print(d.get('my_missing_key', 'key missing!!!!'))
print('missing_key' in d)
print('my_key' in d)

d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
for k in d:
    print(d[k])
for k, v in d.items():
    print(k)
    print(v)

d = {'my_key': 'my_value', 'my_other_key': 'my_other_value'}
del d['my_key']
print(d)
d.pop('my_other_key')
print(d)

from collections import defaultdict

dd = defaultdict(list)
dd['new'].append(1)
dd['new'].append(2)
print(dd)


word_list = ['Python', 'Blog', 'Python', 'Python', 'Dict', 'Dict']
count_dict = defaultdict(int)

for word in word_list:
    count_dict[word] += 1
print(count_dict)