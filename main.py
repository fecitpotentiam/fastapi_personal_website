from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request}
    )


@app.get("/experience")
async def resume(request: Request):
    return templates.TemplateResponse(
        "professional_experience.html", {"request": request}
    )


@app.get("/research")
async def services(request: Request):
    return templates.TemplateResponse(
        "research_experience.html", {"request": request}
    )


@app.get("/honors_and_awards")
async def honors_and_awards(request: Request):
    return templates.TemplateResponse(
        "honors_and_awards.html", {"request": request}
    )


@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse(
        "contact.html", {"request": request}
    )


@app.get("/details")
async def details(request: Request):
    return templates.TemplateResponse(
        "portfolio-details.html", {"request": request}
    )
