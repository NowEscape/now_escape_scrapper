import atexit
import math
from typing import Callable

from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.background import BlockingScheduler

from src.scrapers.amazed.scrapeAmazed import scrape_amazed_theme
from src.scrapers.danPyeonSeon.scrapeDanPyeonSeon import scrap_dps_theme
from src.scrapers.doorEscape.scrapeDoorEscape import scrape_door_escape_theme
from src.scrapers.dumbNdumber.scrapeDumbNdumber import scrape_dumb_n_dumber_theme
from src.scrapers.earthStar.scrapeEarthStar import scrape_earth_star_theme
from src.scrapers.escapeCity.scrapeEscapeCity import scrape_escape_city_theme
from src.scrapers.fantastirck.scrapeFantastrick import scrape_fantastrick_theme
from src.scrapers.goldKey.scrapeGoldKey import scrape_gold_key_theme
from src.scrapers.keyEscape.scrapeKeyEscape import scrape_key_escape_theme
from src.scrapers.masterKey.scrapeMasterKey import scrape_master_key
from src.scrapers.murderParker.scrapeMurderParker import scrape_murder_parker_theme
from src.scrapers.nextEdition.scrapeNextEdition import scrap_next_edition_theme
from src.scrapers.playTheWorld.scrapePlayTheWorld import scrape_play_the_world_theme
from src.scrapers.pointNine.scrapePointNine import scrape_point_nine_theme
from src.scrapers.questionMark.scrapeQuestionMark import scrape_queation_mark_theme
from src.scrapers.roomExCape.scrapeRoomExCape import scrape_room_ex_cape
from src.scrapers.secretCode.scrapeSecretCode import scrape_secret_code_theme
from src.scrapers.secretGardenEscape.ScrapeSecretGarden import scrape_secret_garden_theme
from src.scrapers.sherlockHomes.scrapeSherlockHomes import scrape_sherlock_homes_theme
from src.scrapers.signEscape.scrapeSignEscape import scrape_sign_escape_theme
from src.scrapers.solver.scrapeSolver import scrape_solver_theme
from src.scrapers.xphobia.scrapeXphobia import scrape_xphobia_theme


class ScarpingJob:
    def __init__(self, schedule_id: str, func: Callable):
        self.schedule_id = schedule_id
        self.func = func


SCARPING_JOB_LIST = [
    ScarpingJob(func=scrape_amazed_theme, schedule_id="amazed"),
    # ScarpingJob(func=scrap_dps_theme, schedule_id="dps"),
    ScarpingJob(func=scrape_door_escape_theme, schedule_id="door_escape"),
    ScarpingJob(func=scrape_dumb_n_dumber_theme, schedule_id="dumb_n_dumber"),
    ScarpingJob(func=scrape_earth_star_theme, schedule_id="earth_star"),
    ScarpingJob(func=scrape_escape_city_theme, schedule_id="escape_city"),
    ScarpingJob(func=scrape_fantastrick_theme, schedule_id="fantastrick"),
    ScarpingJob(func=scrape_gold_key_theme, schedule_id="gold_key"),
    # ScarpingJob(func=scrape_key_escape_theme, schedule_id="key_escape"),
    ScarpingJob(func=scrape_master_key, schedule_id="master_key"),
    ScarpingJob(func=scrape_murder_parker_theme, schedule_id="murder_parker"),
    # ScarpingJob(func=scrap_next_edition_theme, schedule_id="next_edition"),
    ScarpingJob(func=scrape_play_the_world_theme, schedule_id="play_the_world"),
    ScarpingJob(func=scrape_point_nine_theme, schedule_id="point_nine"),
    ScarpingJob(func=scrape_queation_mark_theme, schedule_id="queation_mark"),
    ScarpingJob(func=scrape_room_ex_cape, schedule_id="room_ex_cape"),
    ScarpingJob(func=scrape_secret_code_theme, schedule_id="secret_code"),
    ScarpingJob(func=scrape_secret_garden_theme, schedule_id="secret_garden"),
    ScarpingJob(func=scrape_sherlock_homes_theme, schedule_id="sherlock_homes"),
    ScarpingJob(func=scrape_sign_escape_theme, schedule_id="sign_escape"),
    ScarpingJob(func=scrape_solver_theme, schedule_id="solver"),
    ScarpingJob(func=scrape_xphobia_theme, schedule_id="xphobia")
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
    return math.ceil(index / len(SCARPING_JOB_LIST) * 20) % 20


if __name__ == '__main__':
    run()
