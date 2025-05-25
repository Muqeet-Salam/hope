from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Your data
students = [{"name":"uqeQ","marks":96},{"name":"qWQ3e1JcY","marks":5},{"name":"SvtqOUZQi","marks":17},{"name":"h","marks":74},{"name":"FW","marks":91},{"name":"5T4","marks":17},{"name":"jPXWEaat0","marks":86},{"name":"y8RBj","marks":56},{"name":"9biX","marks":14},{"name":"WdX6gkpW","marks":98},{"name":"Qx1F2","marks":37},{"name":"eOT","marks":17},{"name":"9SHFWXNAt","marks":57},{"name":"yaUG7o91IV","marks":88},{"name":"evgy9ym","marks":68},{"name":"2Q58T66","marks":52},{"name":"borj","marks":5},{"name":"0wdat7K","marks":51},{"name":"W8EtCTev","marks":89},{"name":"643","marks":84},{"name":"So","marks":70},{"name":"lbv","marks":53},{"name":"GcWJnI","marks":74},{"name":"atu","marks":1},{"name":"vKlCvabGeX","marks":24},{"name":"5V","marks":28},{"name":"YS3","marks":84},{"name":"Z10P","marks":69},{"name":"sYiNmLRl","marks":48},{"name":"DWjjxNyBb","marks":18},{"name":"rA","marks":20},{"name":"wlxDUgDU","marks":81},{"name":"2","marks":38},{"name":"x","marks":24},{"name":"ylA","marks":62},{"name":"9fj","marks":68},{"name":"BSURlKrs","marks":6},{"name":"qZero1x","marks":35},{"name":"bUQNQY","marks":54},{"name":"M2v","marks":78},{"name":"LRqaLwrerW","marks":13},{"name":"S","marks":90},{"name":"iAVvR34","marks":57},{"name":"T3l","marks":67},{"name":"fuW0","marks":82},{"name":"4","marks":15},{"name":"mjKPrr","marks":8},{"name":"DJv0rWAD6S","marks":60},{"name":"Dewy8MH","marks":88},{"name":"oD7S3vajLY","marks":79},{"name":"8i8qnA","marks":36},{"name":"uZ4z","marks":56},{"name":"qk5","marks":22},{"name":"C","marks":46},{"name":"SDy","marks":89},{"name":"TgK7T6","marks":59},{"name":"vFsLo9FGWf","marks":40},{"name":"s1TiPeZgR","marks":51},{"name":"xHd","marks":96},{"name":"IMIsoH","marks":2},{"name":"kPthT2K","marks":27},{"name":"F","marks":75},{"name":"sebBMTpRI","marks":44},{"name":"DMNdV","marks":80},{"name":"jc3tehPR","marks":33},{"name":"mwI","marks":13},{"name":"L0","marks":34},{"name":"RX4w","marks":91},{"name":"gDHuS","marks":84},{"name":"AP","marks":48},{"name":"yq4Nq","marks":85},{"name":"N","marks":99},{"name":"cLHxy","marks":27},{"name":"wiCcRV","marks":90},{"name":"SAhgpHUL","marks":92},{"name":"Ju2a6bt3lZ","marks":7},{"name":"hFwr","marks":11},{"name":"Sj","marks":17},{"name":"Y5KYnW31x","marks":27},{"name":"NCDoMb","marks":4},{"name":"2SpOq8SX","marks":13},{"name":"p8rR","marks":15},{"name":"HgYLp6ce6m","marks":36},{"name":"c2c","marks":6},{"name":"5wkwGAK","marks":76},{"name":"L","marks":81},{"name":"lh","marks":39},{"name":"d4qzQh","marks":76},{"name":"3CeHj","marks":39},{"name":"FMlzjk","marks":88},{"name":"bL","marks":61},{"name":"aB12p13","marks":44},{"name":"49J1u6KA8","marks":6},{"name":"NN7zBUcq","marks":47},{"name":"b0YLvh7AJP","marks":53},{"name":"fiEZC","marks":53},{"name":"M3UCPmv","marks":75},{"name":"wst","marks":45},{"name":"iLUa","marks":71},{"name":"0M8e25","marks":37}]


# Lookup dictionary for quick access
student_dict = {s["name"]: s["marks"] for s in students}

@app.get("/")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    
    if not names:
        return JSONResponse(
            status_code=400,
            content={"error": "No name parameters provided"}
        )

    marks = [student_dict.get(name, 0) for name in names]
    
    return JSONResponse(content={"marks": marks})
