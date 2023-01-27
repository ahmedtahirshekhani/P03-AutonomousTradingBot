from flask import jsonify
def successMessage(message, data):
    for key in data:
        if isinstance(data[key], float):
            data[key] = str(data[key])
    
    return {
        'success': True,
        'message': message,
        'data': data
    }

def errorMessage(message):
    return {
        'success': False,
        'message': message
    }

