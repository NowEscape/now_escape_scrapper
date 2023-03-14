import atexit
import math
from typing import Callable

from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler

from src.scrapers.keyEscape.scrapeKeyEscape import scrape_key_escape_theme
from src.scrapers.nextEdition.scrapeNextEdition import scrap_next_edition_theme
from src.scrapers.sherlockHomes.scrapeSherlockHomes import scrap_sherlock_homes_theme


class ScarpingJob:
    def __init__(self, schedule_id: str, func: Callable):
        self.schedule_id = schedule_id
        self.func = func


SCARPING_JOB_LIST = [
    ScarpingJob("key_escape", scrape_key_escape_theme),
    ScarpingJob("sherlock_homes", scrap_sherlock_homes_theme),
    ScarpingJob("next_edition", scrap_next_edition_theme),
]


def run():
    scheduler = BlockingScheduler(executors={'default': ProcessPoolExecutor(max_workers=5)}, timezone='Asia/Seoul')
    _ = [scheduler.add_job(job.func,
                           id=job.schedule_id,
                           trigger="cron",
                           minute=f'{0 + to_minute(index)},{20 + to_minute(index)},{40 + to_minute(index)}')
         for index, job in enumerate(SCARPING_JOB_LIST)
         ]

    atexit.register(lambda: scheduler.running and scheduler.shutdown())
    scheduler.start()


def to_minute(index):
    return math.ceil(index / len(SCARPING_JOB_LIST) * 20)


if __name__ == '__main__':
    run()
