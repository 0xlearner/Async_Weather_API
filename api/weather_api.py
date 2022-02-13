from typing import Optional, List
import fastapi
from fastapi import Depends

from models.location import Location
from infrastructure.caching import route_optima
from models.validation_error import ValidationError
from db.data_access_layer.report_dal import Report_DAL
from models.reports import Reports, ReportSubmittal
from depends import get_report_db

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    try:
        return await route_optima(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as e:
        return fastapi.Response(content=str(e), status_code=500)


@router.post("/api/report", name="add_report", status_code=201, response_model=Reports)
async def submit_report(
    report_submittal: ReportSubmittal, reports: Report_DAL = Depends(get_report_db)
):
    return await reports.create_report(report_submittal)


@router.get("/api/all_reports", name="all_reports", response_model=List[Reports])
async def get_report(reports: Report_DAL = Depends(get_report_db)):
    return await reports.get_all_reports()


# return await route_optima(loc.city, loc.state, loc.country, units)
# location = {
#     "city": loc.city,
#     "state": loc.state,
#     "country": loc.country,
#     "units": units,
# }
# in_cache = redis_client.get(json.dumps(location))
# print(type(in_cache))
# if in_cache:
#     report = json.loads(in_cache.decode("utf-8"))
#     print(type(report))
#     # report = json.loads(report)
#     # print(type(report))
# else:
#     report = await get_report(loc.city, loc.state, loc.country, units)
# redis_client.set(json.dumps(location), json.dumps(report))
# # print(type(report))
# return report
