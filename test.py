import datetime
import time
from pyfunvice import app_service, start_app, app_service_get


@app_service(path="/api/v1/greet", inparam_type="dict")
async def v1_greet(data: dict) -> dict:
    name = data["name"]
    age = data["age"]
    time.sleep(10)
    return {"name": name, "age": age, "status": "success"}


@app_service(path="/api/v2/greet", inparam_type="flat")
def v2_greet(name: str, age: str) -> dict:
    return {"name": name, "status": "success"}


@app_service(path="/api/v1/upload", body_type="form-data")
def v1_upload(file_name: str) -> dict:
    return {"name": file_name, "status": "success"}


@app_service_get(path="/health")
async def health(data: dict) -> dict:
    time_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"timestamp": time_string}


if __name__ == "__main__":
    start_app(workers=1, max_concurrent=2)
