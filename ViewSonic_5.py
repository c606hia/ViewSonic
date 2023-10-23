import docx
import pandas as pd

born = {
'A': '台北市',
'B': '台中市',
'C': '基隆市',
'D': '台南市',
'E': '高雄市',
'F': '新北市',
'G': '宜蘭縣',
'H': '桃園市',
'I': '嘉義市',
'J': '新竹縣',
'K': '苗栗縣',
'M': '南投縣',
'N': '彰化縣',
'O': '新竹市',
'P': '雲林縣',
'Q': '嘉義縣',
'T': '屏東縣',
'U': '花蓮縣',
'V': '台東縣',
'W': '金門縣',
'X': '澎湖縣',
'Z': '連江縣',
'L': '台中縣',
'R': '台南縣',
'S': '高雄縣',
'Y': '陽明山管理局'
}

doc = docx.Document('身分資料文件.docx')
members_data = []

for i in doc.paragraphs:
    data = i.text.replace(',', ' ').split()
    if data:
        members_data.append(data)
    # members.append([name, first, ID])

df = pd.DataFrame(members_data,columns=['姓','名','身份證'])
df['性別'] = df['身份證'].str[1].apply(lambda x: 'Male' if x == '1' else 'Female')
df['戶籍地'] = df['身份證'].str[0].apply(lambda x: born.get(x, 'None'))

df = df[['姓','名','性別','身份證','戶籍地']]
df.to_excel("應用測驗.xlsx", index=False)

