import scrapy

from stockstar.items import StockstarItemLoader, StockstarItem


class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/ranklist_a_3_1_1.html']

    # datalist > tr:nth-child(1) > td:nth-child(1) > a
    # datalist > tr:nth-child(1) > td:nth-child(3)
    # datalist > tr:nth-child(1) > td.align_right.select
    def parse(self, response):
        page = int(response.url.split('_')[-1].split('.')[0])
        item_nodes = response.css('#datalist tr')
        for item_node in item_nodes:
            item_loader = StockstarItemLoader(item=StockstarItem(), selector=item_node)
            item_loader.add_css('code', 'td:nth-child(1) a::text')
            item_loader.add_css('abbr', 'td:nth-child(2) a::text')
            item_loader.add_css('tradeValue', 'td:nth-child(3)::text')
            item_loader.add_css('totalValue', 'td.align_right.select::text')
            stock_item = item_loader.load_item()
            yield stock_item
        if item_nodes:
            next_page = page + 1
            next_url = response.url.replace('{0}.html'.format(page), '{0}.html'.format(next_page))
            yield scrapy.Request(url=next_url, callback=self.parse)