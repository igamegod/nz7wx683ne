from mitmproxy import http
import json

CONFIG_FILE = "Config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"description": "Default description", "title": "Default title"}

def response(flow: http.HTTPFlow):
    config = load_config()

    if flow.request.url == "https://www.epicgames.com/account/v2/ajax/redemption/validate-redemption-code":
        flow.response.text = f'''
        {{
            "data": {{
                "description": "{config['description']}",
                "entitlementName": "",
                "namespace": "",
                "offerId": "",
                "title": "{config['title']}"
            }},
            "isSuccess": true,
            "numericErrorCode": null,
            "success": true
        }}
        '''
    
    elif flow.request.url == "https://www.epicgames.com/account/v2/ajax/redemption/submit-redemption-code":
        flow.response.text = '''
        {
            "code": "",
            "isSuccess": true,
            "message": "",
            "numericErrorCode": null
        }
        '''
