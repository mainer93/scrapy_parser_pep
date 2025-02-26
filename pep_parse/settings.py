BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True
FEED_EXPORT_ENCODING = 'utf-8'
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'overwrite': False,
        'fields': ['number', 'name', 'status'],
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
