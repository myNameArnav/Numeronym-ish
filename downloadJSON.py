def downloadIPAJson():
    import requests

    JSON_URL = "https://www.internationalphoneticalphabet.org/ipa-translator-files/ipa-translator-english-v1/en_US.json"

    payload = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/500.0"
    }

    response = requests.request("GET", JSON_URL, data=payload, headers=headers)

    with open("IPA.json", "w", encoding="utf-8") as f:
        f.write(response.text)
