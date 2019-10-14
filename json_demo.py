import json

json_obj = """
{
"widget": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}    
"""

# converting json to py obj
data = json.loads(json_obj)
print(data["widget"]["image"]["src"])

# converting py obj to json
del data["widget"]["text"]["style"]     # deleting style form text from widget

new_json_obj = json.dumps(data)         # json.dumps converts py obj back to json
print(data)



