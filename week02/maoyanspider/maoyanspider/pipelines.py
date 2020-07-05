# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql.cursors


class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        print('glxe-glxe-glxe-glxe-glxe-glxe-glxe-glxe')
        title = item['title']
        t = item['type']
        time = item['time']



        # Connect to the database
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        print(connection)

        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `maoyan` (`title`, `type`, `time`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (title, t, time))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()

        return item
