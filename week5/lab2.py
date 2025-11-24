import pandas as pd

df  = pd.read_csv("company_salaries.csv" ,encoding='utf-8')

new_data = [
    {"職位": "資訊處處長", "年資": 8, "薪水": 70560, "學歷": "博士", "性別": "男", "年齡": 37},
    {"職位": "保全", "年資": 4, "薪水": 34000, "學歷": "碩士", "性別": "男", "年齡": 53},
    {"職位": "工程師", "年資": 13, "薪水": 153000, "學歷": "碩士", "性別": "男", "年齡": 38}
]

add_data = pd.DataFrame(new_data)

merge = pd.concat([df,add_data], ignore_index=True)
merge.to_csv('output.csv',index=False, encoding='utf-8')


idx1 = merge['學歷'].mode()[0]
idx2 = merge['性別'].mode()[0]

print(f"公司總人數：{len(merge)}人")
print(f"最多人的學歷：{idx1}")
print(f"最多人的性別：{idx2}")