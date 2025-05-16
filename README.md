# Image crawler 

- Crawling images from Google based on reference image, reference description text.
- Based on the ViT-B-32 model, cosine similarity is used to determine the similarity between images

---

<br>

`reference image`

<img src = "https://github.com/user-attachments/assets/6e870108-a7c6-4a85-ac64-eeb2dfdef0c6" width="15%" height="15%">

<br>


### example code
```python
from image_crawler import get_image, create_refereces_object, classify_all_image

images = get_image('pepe', '/Users/username/Desktop/finder/geckodriver', scroll=0) # list[base64 string]

ref_object = create_refereces_object(
    references_image=[
        '# reference image url'
    ],
    references_text=[
    ]
)

imgs = classify_all_image(images, ref_object, threshold=0.7) # list[base64 string]
```
---

<br><br>

##### Unclassified Images ( images ) - google images (crawl)
<img src = "https://github.com/user-attachments/assets/5c5b860e-a911-4ecb-bb91-eb6cd9252a87" width="30%" height="30%">

##### classified Images ( imgs )
<img src = "https://github.com/user-attachments/assets/dd502e90-4771-4ac2-ba1d-2cb9d7e12a2e" width="30%" height="30%">
