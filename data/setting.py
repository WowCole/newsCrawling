from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup as bs
import data.publisher as pb

import data.tools as tools

#네이버 세팅
dateRange=tools.date_range("20221108","20221108")


category_code =[ i for i in range(1,400)]
