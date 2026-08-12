import requests

def call_bot(prompt: str) -> str:
    url = "http://localhost:8000/chat"
    try:
        res = requests.post(url, json={"prompt": prompt})
        if res.status_code == 200:
            return res.json().get("response", "")
        return f"Error: {res.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

