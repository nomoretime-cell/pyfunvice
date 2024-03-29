from pyfunvice import faas, start_faas


@faas(path="/api/v1/greet")
async def v1_greet(data: dict) -> dict:
    name = data["name"]
    age = data["age"]
    return {"name": name, "age": age, "status": "success"}


@faas(path="/api/v2/greet", inparam_type="flat")
async def v2_greet(name: str, age: str) -> dict:
    return {"name": name, "status": "success"}


@faas(path="/api/v1/upload", body_type="form-data")
async def v1_upload(file_name: str) -> dict:
    return {"name": file_name, "status": "success"}


if __name__ == "__main__":
    start_faas(workers=1)
