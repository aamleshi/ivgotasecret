#Arash Amleshi 4/8/2020 (presented by the quarentine)
"""This function scrapes google.com to construct a spreadsheet of secrets page candidates
"""
from tqdm import tqdm
import numpy as np 
import pandas as pd 
import argparse
import googlesearch
import re

def googleSearchCleanup(urlList, regex):
    #Cleans up the list of searched posts to only include uniques at top level
    cleanSet = set()
    for url in urlList:
        cleanSet.add(regex.search(url).group(1))
        #print(regex.search(url).group(0), regex.search(url).group(1))
    print(cleanSet)

def googleSearch(query, n):
    #returns top N results for searched string
  
    return [result for result in googlesearch.search(query,
        num=n,
        stop=n,
        pause=2)] 

def main(schoolFile):
    with open(schoolFile, 'r') as schoolList:
        schoolList = [line.strip('\n') for line in schoolList.readlines()]
    search = googleSearch("site:facebook.com "+ "University of Chicago" +" Secrets", 10)
    print(search)
    regex = re.compile('(.+?[\/][\/].+?[\/].+?[\/]+?)(.*)')
    googleSearchCleanup(search, regex)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("schoolList")
    args = parser.parse_args()
    main(args.schoolList)