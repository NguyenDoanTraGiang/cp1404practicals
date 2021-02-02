import wikipedia

search_phrase = input("Enter a search_phrase: ")
while not search_phrase == "":
    try:
        page = wikipedia.page(search_phrase)
        summary = wikipedia.summary(search_phrase)
        print("Summary: ", summary)
        print("Title: ", page.title)
        print("URL: ", page.url)
        search_phrase = input("Enter a search_phrase: ")
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options
        print(options)

