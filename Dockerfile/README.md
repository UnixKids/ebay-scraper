Creates a docker image from the eBay scraper. The TERM variable defines the product that's searched. The csv file is outputted to the /ebay/ directory. Example usage:

docker run -e "TERM=iPhone" --mount type=bind,source=/mnt,target=/ebay ebay-scraper
