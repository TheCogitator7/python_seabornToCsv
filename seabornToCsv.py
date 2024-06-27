import seaborn as sns
import openpyxl


#seaborn의 데이터를 불러들임

df=sns.load_dataset('titanic')

#titanic 의 10행을 출력

print(df.head(10))

#seaborn lib의 titanic 데이터를 csv 파일로 만듦

df.to_csv('./titanic.csv', index=False)

#seaborn lib의 titanic 데이터를 excel 파일로 만듦
#openpyxl module 불러들임

df.to_excel('./titanic.xlsx', index=False)
