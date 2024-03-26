from pyfunvice import faas, faas_with_dict_req, start_faas


@faas(path="/a")
def greet2(name: str) -> dict:
    return {"name": name, "status": "success"}


@faas_with_dict_req(path="/b")
def greet(data: dict) -> dict:
    name = data["name"]
    age = data["age"]
    return {"name": name, "age": age, "status": "success"}


if __name__ == "__main__":
    start_faas(workers=1)
