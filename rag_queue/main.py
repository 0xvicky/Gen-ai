from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queue.worker import process_queue

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/chat")
def chat(query: str):
    job = queue.enqueue(process_queue, query)
    return {"status": "queued", "job_id": job.id}


@app.post("/get-result")
def get_result(job_id: str = Query(..., description="This is job id")):
    job = queue.fetch_job(job_id=job_id)
    if job is None:
        print("Job not found")
    else:
        result = job.return_value()
        print(result)
        return result


# {
#   "status": "queued",
#   "job_id": "deaa248c-bef2-4fc9-ad73-5afd5295b4a5"
# }
