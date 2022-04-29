'''
- File Name: main.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 29] File Version 1.0
'''

import re, usecsv

english = 'She is a vegetarian. She does not eat meat. she thinks that animals should not be killed. It is hard for her to hang out with people. Many people like to eat meat. She told his parents not to have meat. They laughed at her. She realized they couldn\'t give up meat.'
korean = '그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다. 그녀는 동물을 죽여서는 안 된다고 생각합니다. 그녀는 사람들과 어울리는 것이 어렵습니다. 많은 사람들이 고기를 먹고 싶어합니다. 그녀는 그의 부모에게 고기를 먹지 말라고 말했다. 그들은 그녀를 웃었다. 그녀는 고기를 포기할 수 없다는 것을 깨달았습니다.'

english_list = re.split('\.', english)
korean_list = re.split('\.', korean)

total = []

for i in range(len(english_list)):
    total.append([english_list[i], korean_list[i]])

usecsv.writecsv('english_korean.csv', total)