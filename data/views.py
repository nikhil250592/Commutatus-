from django.shortcuts import render

from bs4 import BeautifulSoup
import urllib2

 def moview( request)
     url = "http://www.imdb.com/chart/?ref_=nv_ch_cht_2

     data = urllib2.urlopen(url).read()
     page = BeautifulSoup(data, 'html.parser')

     rows = page.findAll("tr", {})
  
   for tr in rows:
       for data in tr.findAll("td", {}):
           return("index.html",{data:data},context)
