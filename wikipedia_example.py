import wikipedia

if __name__ == "__main__":
    wikipedia.set_lang("de")
    print(wikipedia.summary("Limburger Dom"))
    limburgerDom = wikipedia.page("Limburger Dom")
    print(limburgerDom.images)
    print(limburgerDom.coordinates)
