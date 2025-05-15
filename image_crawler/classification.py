import torch, open_clip

from .type import base64Type, urlType
from .utils import base64ToImage, urlToBase64


device = 'cpu'
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')
model = model.to(device).eval()



def embedImage(base64_image: base64Type):
    with torch.no_grad():

        if ',' in base64_image: base64_image = base64_image.split(',')[1]
        img = base64ToImage(base64_image)
        return model.encode_image(preprocess(img).unsqueeze(0).to(device))


def embedText(text: str):
    return model.encode_text(tokenizer([text]).to(device))


def create_refereces_object(references_image: list[urlType]=[], references_text: list[str]=[]):

    image_embed = [embedImage(urlToBase64(url)) for url in references_image]
    text_embed = [embedText(text) for text in references_text]

    ref = image_embed + text_embed
    ref = torch.cat(ref).mean(dim=0, keepdim=True)
    ref /= ref.norm(dim=-1, keepdim=True)

    return ref.T


def classify_image(image: base64Type, refereces_object):
    image_embed = embedImage(image)
    image_embed /= image_embed.norm(dim=-1, keepdim=True) 

    return (image_embed @ refereces_object).item()


def classify_all_image(images: list[base64Type], refereces_object, threshold=0.8):
    
    img = []
    for i in images:
        similarity = classify_image(i, refereces_object)
        if similarity >= threshold: img.append(i)
    
    return img