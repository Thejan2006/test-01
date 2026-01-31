# https://picsum.photos/id/237/200/300

import requests


def get_image_url(count):
    if count <= 0 :
        print("Count must be a positive integer.")
        return None
    for i in range(0,count):
        url = f"https://picsum.photos/id/{i}/200/300"
        yield url
        
urls = get_image_url(10)     
for  i,url in enumerate(urls):
    r = requests.get(url, stream=True)
    
    if r.status_code == 200:

      files= f"image/{i}.jpg"
      with open(files, "wb") as file:
        file.write(r.content)
      print("downlad complete", files)
    else:
      print("Error:", r.status_code)