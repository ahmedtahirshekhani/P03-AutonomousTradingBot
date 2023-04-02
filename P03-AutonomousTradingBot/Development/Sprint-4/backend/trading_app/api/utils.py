def successMessage(message, data):
    # if isinstance(data, list):
    #     return {"success": True, "message": message, "data": data}

    # for key in data:
    #     if isinstance(data[key], float):
    #         data[key] = str(data[key])

    return {"success": True, "message": message, "data": data}


def errorMessage(message):
    return {"success": False, "message": message}
