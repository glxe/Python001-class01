# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        print('glxe-glxe-glxe-glxe-glxe-glxe-glxe-glxe')    
        title = item['title']
        t = item['type']
        time = item['time']
        output = f'|{title}|\t|{t}|\t|{time}|\n\n'
        with open('./maoyanUseXpath.txt', 'a+', encoding='utf-8') as artical:
            artical.write(output)
            artical.close()
        return item
