import csv,sys,os
project_dir = "db_stock"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()
from home.models import stock_info
data = csv.reader(open("NewTotalCompany.csv", encoding="utf-8"),delimiter=",",)
for row in data:
	if row[0] != 'id':
		unit = stock_info()
		unit.stock_id = row[4]
		unit.stock_name = row[5]
		unit.industry = row[3]
		unit.save()