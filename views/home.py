import fastapi
from fastapi import Depends
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

from db.data_access_layer.report_dal import Report_DAL
from depends import get_report_db

router = fastapi.APIRouter()


templates = Jinja2Templates("templates")


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request})


@router.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
