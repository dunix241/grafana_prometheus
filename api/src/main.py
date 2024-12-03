from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prom import Blackbox

app = FastAPI()
BL_BOX_FILE = "/prometheus/blackbox_targets.yml"

blackbox = Blackbox(BL_BOX_FILE)
ALLOWED_TOKENS = ["xxxx"]


# enable authen x-request-token header
async def auth_middleware(request: Request, call_next):
    # Perform your authorization logic here
    if "x-request-token" not in request.headers:
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})

    provided_token = request.headers["x-request-token"]

    if provided_token not in ALLOWED_TOKENS:
        return JSONResponse(status_code=401, content={"message": "Invalid token"})

    response = await call_next(request)
    return response


# authorize function
@app.middleware("http")
async def middleware(request: Request, call_next):
    response = await auth_middleware(request, call_next)
    return response


@app.get("/api/v1/blackbox")
async def get_blackbox_targets():
    return blackbox.get_targets()


@app.post("/api/v1/blackbox/add")
async def update_target(instance_name: str):
    new = blackbox.update_target(instance_name)
    return new


@app.post("/api/v1/blackbox/remove")
async def remove_target(instance_name: str):
    new = blackbox.remove_target(instance_name)
    return new
