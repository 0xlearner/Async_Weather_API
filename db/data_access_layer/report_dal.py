import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.future import select

from db.models.report import Report
from models.reports import ReportSubmittal


class Report_DAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

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
