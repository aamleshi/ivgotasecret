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
import time
import os

def updateSchoolList2File(schools, filepath):
    if not os.path.exists(filepath):
        return schools
    with open(filepath,'r') as f:
        lastLine = f.readlines()[-1]
        lastSchool = lastLine.split(',')[0]
    return schools[schools.index(lastSchool)+1:]

def scrapeCSV(schools, site, groupType, regex, n=5):
    #Creates a csv for a website/grouptype permutation
    outfilename = "rawScraped/"+site[:-4]+groupType+".csv"

    schools = updateSchoolList2File(schools, outfilename)
    
    
    for school in tqdm(schools):
        with open(outfilename, 'a') as outfile:
            raw_scrape = googleSearch("site:"+site + " " + school + " " +groupType, n)
            clean_scrape = googleSearchCleanup(raw_scrape, regex)
            print(school)
            outfile.write(school+',' + ",".join(clean_scrape)+'\n')

def googleSearchCleanup(urlList, regex):
    #Cleans up the list of searched posts to only include uniques at top level
    cleanSet = set()
    for url in urlList:
        if url[-1] != '/':
            url = url+'/'
        cleanSet.add(regex.search(url).group(1))
    return(list(cleanSet))

def progressiveBackoff(i):
    return 15*i*60

def googleSearch(query, n):
    #returns top N results for searched string
    tries = 1
    user_agent = googlesearch.get_random_user_agent()
    while True:
        try:
            results = googlesearch.search(query,num=n,stop=n,pause=20, user_agent = user_agent)
            return [result for result in results]
        except:
            timeout = progressiveBackoff(tries)
            print("timeout:" , timeout)
            time.sleep(timeout)
            tries += 1

        

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