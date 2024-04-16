def test():
    import requests, json
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk22506-ffnUL4X7JxFOgnZlE4MIT3BlbkFJbmQUPz6UNicJAEjwZMvo',
        "api_key": "sk22506-ffnUL4X7JxFOgnZlE4MIT3BlbkFJbmQUPz6UNicJAEjwZMvo"
    }

    data = {
        "api_key": "sk22506-ffnUL4X7JxFOgnZlE4MIT3BlbkFJbmQUPz6UNicJAEjwZMvo",
    }
    history = []

    while True:
        user_input = input("> ")
        history.append({"role": "user", "content": user_input})
        data["history"] = history
        print(data)
        response = requests.post('http://localhost:5000/chat/v1/completions', data=json.dumps(data), headers=headers)

        rdata = eval(response.text)
        history.append({"role": "assistant", "content": rdata["text"]})
        print(f"[{rdata["role"]}]", rdata["text"])

test()