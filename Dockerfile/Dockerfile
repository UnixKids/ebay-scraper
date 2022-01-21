FROM python:3.8
RUN mkdir /ebay/
ADD ebay-scraper.py .
RUN pip install requests bs4 pandas
CMD ["python", "ebay-scraper.py"]
