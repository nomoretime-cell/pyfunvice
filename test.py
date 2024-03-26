from pyfunvice import faas, faas_with_dict_req, start_faas


@faas(path="/api/v1/greet")
def v1_greet(name: str) -> dict:
    return {"name": name, "status": "success"}


@faas_with_dict_req(path="/api/v2/greet")
def v2_greet(data: dict) -> dict:
    name = data["name"]
    age = data["age"]
    return {"name": name, "age": age, "status": "success"}


if __name__ == "__main__":
    start_faas(workers=1)
