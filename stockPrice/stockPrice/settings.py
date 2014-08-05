# Scrapy settings for stockPrice project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'stockPrice'

SPIDER_MODULES = ['stockPrice.spiders']
NEWSPIDER_MODULE = 'stockPrice.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stockPrice (+http://www.yourdomain.com)'
