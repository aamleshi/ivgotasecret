#Arash 4/10/2020
#This script takes in the path to rawScraped, and aggregates relevant ones


def main(rawFolder):


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("rawFolder")
    args = parser.parse_args()
    main(args.rawFolder)

#https://medium.com/analytics-vidhya/the-art-of-not-getting-blocked-how-i-used-selenium-python-to-scrape-facebook-and-tiktok-fd6b31dbe85f