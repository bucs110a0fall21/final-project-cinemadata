import requests
class MoviePoster:
    def __init__(self, url, save_path):
        '''
        Requests for image and saves image to path/folder being used
        args:
            (str) url - the url used to get the image from the API
            (str) save_path - the directory that will be used to save the image will be saved to and sets file name of the saved image
        return: None
        '''
        self.url = url
        self.save_path = save_path
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            file.close()
