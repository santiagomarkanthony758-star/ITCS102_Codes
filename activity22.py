
anime_type = ["isekai", "adventure", "scifi", "manwha"]
animetitle = []

while True:
    ans = input("Do you know any anime ---> (yes / no)")

    if ans.lower() == "yes":
        print("what is its type -- ? select from the list ")
        for x in anime_type:
            print(x) #traversing a list
        a_type = input("type --> ")

        title = input("what is the title of the anime > ")
        anime_title = append(title)
        continue
    else:
        print("thank your po aray kopo ")
        print("so  far you have encode")
        for x in anime_title:
            print("x") #traversing a list
        break