import csv

from collections import defaultdict
from datetime import datetime

from .constants import BASE_DIR, DATE


class PepParsePipeline:
    def __init__(self) -> None:
        self.results = BASE_DIR / 'results'
        self.results.mkdir(parents=True, exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.status_count.values())
        filename = f"status_summary_{datetime.now().strftime(DATE)}.csv"
        with open(f"{self.results}/{filename}",
                  mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Status', 'Count'])
            for status, count in self.status_count.items():
                writer.writerow([status, count])
            writer.writerow(['Total', total])
