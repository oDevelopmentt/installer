import requests
def download_file(url):
    response = requests.get(url)
    if "content-disposition" in response.headers:
        content_disposition = response.headers["content-disposition"]
        filename = content_disposition.split("filename=")[1]
    else:
        filename = url.split("/")[-1]
    with open(filename, mode="wb") as file:
        file.write(response.content)
    print(f"Downloaded file {filename}")
