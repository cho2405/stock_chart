import FinanceDataReader as fdr
import pandas as pd


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db_chart.settings")
import django
django.setup()


from app.models import KospiPredict

def get_stock_daily(name, no, date):
	df = fdr.DataReader(no, date).reset_index()
	df['Name'] = name
	return df


if __name__ == '__main__':

	df = get_stock_daily('삼성전자', '005930', '2020')
	
	for index, row in df.iterrows():
		KospiPredict(name=row['Name'], date=row['Date'], open=row['Open'], close=row['Close']).save()
