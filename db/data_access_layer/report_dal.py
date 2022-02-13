import datetime
from typing import List, Optional
import json

from sqlalchemy.orm import Session
from sqlalchemy.future import select

from db.models.report import Report
from db.models.weather import Weather
from models.reports import ReportSubmittal
from infrastructure.caching import (
    get_routes_from_cache,
    set_routes_to_cache,
)
from services.openweather_service import get_report
from models.location import Location


class Report_DAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_weather(
        self, weather_loc: Location, units: Optional[str] = "metric"
    ) -> Weather:

        cache = get_routes_from_cache(key=weather_loc.__dict__)

        if cache:
            data = json.loads(cache.decode("utf-8"))
            data_dict = json.loads(data)
            data_dict["cache"] = True
            return data_dict

        else:

            forecast = await get_report(
                weather_loc.city, weather_loc.state, weather_loc.country, units
            )
            weather = Weather(
                **weather_loc.dict(),
                temperature=forecast["temp"],
                units=units,
                created_date=datetime.datetime.now()
            )
            self.db_session.add(weather)
            await self.db_session.flush()
            forecast["cache"] = False
            data = json.dumps(forecast)
            state_res = set_routes_to_cache(key=weather_loc.__dict__, value=data)

            if state_res is True:
                return json.loads(data)

        return weather

    async def create_report(self, report_submittal: ReportSubmittal) -> Report:
        report = Report(**report_submittal.dict(), created_date=datetime.datetime.now())
        self.db_session.add(report)
        await self.db_session.flush()
        return report

    async def get_all_reports(self) -> List[Report]:
        query = await self.db_session.execute(
            select(Report).order_by(Report.created_date.desc())
        )
        return query.scalars().all()
