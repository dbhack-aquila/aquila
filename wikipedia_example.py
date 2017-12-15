import wikipedia
import re


def get_first_image(wikipedia_page):
    htmlcode = wikipedia_page.html()
    imgcode = re.search('<img.*src=".*".*/>', htmlcode).group(0)
    imagecode_array = imgcode.split()
    for imagecode_part in imagecode_array:
        if "src=" in imagecode_part:
            imagecode_array = imagecode_part.split('"')
            break
    for imagecode_part in imagecode_array:
        if "//" in imagecode_part:
            image_url = "https:"+ imagecode_part.split("thumb/")[0] + imagecode_part.split("thumb/")[1].rsplit("/",1)[0]
            return image_url


if __name__ == "__main__":
    wikipedia.set_lang("de")
    print(wikipedia.summary("Limburger Dom"))
    limburgerDom = wikipedia.page("Limburger Dom")
    print(limburgerDom.images)
    print(limburgerDom.coordinates)
    htmlpage = limburgerDom.html()
    image = re.search('<img.*src=".*".*/>', htmlpage)
    image.group(0)
    print(image.group(0))
    print(get_first_image(limburgerDom))


