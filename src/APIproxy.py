import requests
class MoviePoster:
    def __init__(self, url, save_path):
        '''
        requests for image and saves image to path/folder being used
        Args:
            self
            url (str) the url used to get the image from the API
            save_path (str) the directory that will be used to save the image will be saved to and sets file name of the saved image
        '''
        self.url = url
        self.save_path = save_path
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            file.close()
