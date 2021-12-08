import requests
class MoviePoster:
    def __init__(self, url, save_path):
        self.url = url
        self.save_path = save_path
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            file.close()
