# god i hate python's datetime package
from datetime import date
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.requests import Request
from starlette.routing import Route
import uvicorn

# time since friends
delta = date.today() - date(2017, 12, 26)

async def home(request: Request):
    return PlainTextResponse(str(delta.days))

app = Starlette(debug=False, routes=[
    Route('/', home)
])

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")