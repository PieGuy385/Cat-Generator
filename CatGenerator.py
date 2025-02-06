import requests
Cont = True
def cat_generator():
    response = requests.get(
        "https://api.thecatapi.com/v1/images/search?api_key=live_pQxEga8SYutrBtIjODEwTkLvTf4eSC8ZGc7u0Pqt6iF7pseDMenLdrbExymX6BV4")
    data = response.json()
    print(data[0]['url'])


while Cont == True:
    cat_generator()
    while Cont == True:
        yn = input("Would you like to continue? (y/n): ")
        if yn.lower() == "y":
            Cont = True
            break
        elif yn.lower() == "n":
            Cont = False
            break
        else:
            print("Please enter \"y\" or \"n\"")

print("I hope you enjoyed the cat pics :)")

