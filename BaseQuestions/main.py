from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import models, modules


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/rating/questionare/")
async def post_results(results: models.QuestionareResults):
    if modules.check_user_exist(email=results.email):
        defined_type = modules.check_questionare(results.ans)

        modules.set_value_user("ptype", defined_type.matched, results.email)

        return {"ok": True, "matched": defined_type.matched}

    else:
        return HTTPException(status_code=404, detail="User not found :(")

@app.get("/rating/questionare/")
async def get_results(user: models.OnlyUser):
    if modules.check_user_exist(email=user.email):
        ptype = modules.get_value_user(user.email, "ptype")

        return {"ok": True, "matched": ptype}

    else:
        return HTTPException(status_code=404, detail="User not found :(")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
