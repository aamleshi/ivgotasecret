#Arash Amleshi 4/8/2020 (presented by the quarentine)
"""This function scrapes google.com to construct a spreadsheet of secrets page candidates
"""
from tqdm import tqdm
import numpy as np 
import pandas as pd 
import argparse
import googlesearch
import re
import csv

def scrapeCSV(schools, site, groupType, regex, n=5):
    #Creates a csv for a website/grouptype permutation
    outfilename = site[:-4]+groupType+".csv"
    with open("rawScraped/"+outfilename, 'w') as outfile:
        for school in tqdm(schools):
            raw_scrape = googleSearch("site:"+site + " " + school + " " +groupType, n)
            clean_scrape = googleSearchCleanup(raw_scrape, regex)
            outfile.write(school+',' + ",".join(clean_scrape)+'\n')

def googleSearchCleanup(urlList, regex):
    #Cleans up the list of searched posts to only include uniques at top level
    cleanSet = set()
    for url in urlList:
        if url[-1] != '/':
            url = url+'/'
    return(list(cleanSet))

def googleSearch(query, n):
    #returns top N results for searched string
  
    return [result for result in googlesearch.search(query,
        num=n,
        stop=n,
        pause=2)] 

def main(schoolFile):
    with open(schoolFile, 'r') as schoolList:
        schoolList = [line.strip('\n') for line in schoolList.readlines()]
    
    Sites = ['facebook.com', 'twitter.com']
    groupTypes = ["crushes", "secrets", "confessions"]
    regex = re.compile('(.+?[\/][\/].+?[\/].+?[\/]+?)(.*)')

    for site in Sites:
        for groupType in groupTypes:
            print(site, groupType)
            scrapeCSV(schoolList, site, groupType, regex)
            

    
    
    search = googleSearch("site:facebook.com "+ "University of Chicago" +" Secrets", 10)
    print(search)
    
    googleSearchCleanup(search, regex)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("schoolList")
    args = parser.parse_args()
    main(args.schoolList)