from db.session import async_engine
from db.data_access_layer.report_dal import Report_DAL


async def get_report_db():
    async with async_engine() as session:
        async with session.begin():
            yield Report_DAL(session)
