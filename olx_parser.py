from bs4 import BeautifulSoup
import requests
import urllib.request


def link_generator_for_search_by_keyword(link_category: str, keywords: str):
    words = keywords.split(" ")
    link = link_category + "q-" + "-".join(words)
    return link


def link_generator_by_subcategory(category: str, subcategory=""):
    if subcategory != "":
        link = "https://www.olx.ua/" + category + "/" + subcategory + "/"
    else:
        link = "https://www.olx.ua/" + category + "/"

    return link


def get_links_from(link: str):
    req = requests.session().get(link)
    soup = BeautifulSoup(req.text, "lxml")
    all_td = soup.find_all("td", class_="photo-cell")
    links = []
    for td in all_td:
        links.append(td.find("a").get("href"))
    return links


def price_link(link: str, price_a_from="", num_a_from="", price_a_to="", num_a_to=""):
    if price_a_from == "":
        price_link_ = link + f"?search[filter_float_price%{num_a_to}]Ato]={price_a_to}"
    elif price_a_to == "":
        price_link_ = link + f"?search[filter_float_price%{num_a_from}Afrom]={price_a_from}"
    else:
        price_link_ = link + f"?search[filter_float_price%{num_a_from}Afrom]={price_a_from}&search[filter_float_price%{num_a_to}Ato]={price_a_to} "

    return price_link_


class OLXAdvParser:
    def __init__(self, url: str, bearer: str):
        self.url = url
        self.headers = {
            'Authorization': bearer}

    def get_name_of_adv(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        name_of_adv = soup.find("h1", class_="css-r9zjja-Text eu5v0x0").text
        return name_of_adv

    def get_date_of_publ(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        date_of_publ = soup.find("span", class_="css-19yf5ek").text
        return date_of_publ

    def get_photo(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        img_url = soup.find("img").get("src")
        img = urllib.request.urlopen(img_url).read()
        with open("img.jpg", "wb") as out:
            out.write(img)
        return 1

    def get_date(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        date_registr = soup.find("div", class_="css-1bafgv4-Text eu5v0x0").text
        return date_registr

    def get_name(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        name_of_user = soup.find("h2", class_="css-u8mbra-Text eu5v0x0").text
        return name_of_user

    def get_views(self):
        req = requests.session().get(self.url, headers=self.headers)
        soup = BeautifulSoup(req.text, "lxml")
        views = soup.find("div", class_="css-1ferwkx").find("span", class_="css-1qvxqpo")
        return views

    def get_price(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        price = soup.find("h3", class_="css-okktvh-Text eu5v0x0").text
        try:
            negotiable_or = soup.find("p", class_="css-1897d50-Text eu5v0x0").text
        except Exception:
            negotiable_or = ""
        return price + negotiable_or

    def get_quantity(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        new_url = soup.find("a", class_="css-14vo8cu").get("href")

        if new_url.startswitch("https:"):
            pass
        else:
            link = "https://www.olx.ua/" + soup.find("a", class_="css-14vo8cu").get("href")
            req_for_quan = requests.get(link)
            soup_for_quan = BeautifulSoup(req_for_quan.text, "lxml")
            quantity = soup_for_quan.find_all("li")

            return quantity

    def get_phone(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "lxml")
        id = soup.find("div", class_="css-1ferwkx").find("span").text.split(" ")[-1]
        check_page = requests.get("https://www.olx." + "ua" + "/api/v1/offers/" + id + "/phones/",
                                  headers=self.headers)  # "Bearer 93684d4be62a2a7de3838c366011597ce676074d"
        checked = check_page.text
        return checked.split('"')[-2]


# https://www.olx.ua/api/v1/offers/740762310/phones/

list_links = get_links_from("https://www.olx.ua/detskiy-mir/detskaya-odezhda/")
for i in list_links[0:1]:
    print(i)
    user = OLXAdvParser(i, bearer="Bearer af71501ae28c1acf1d6da52f92bb5ba48904e90e")
    print(user.get_photo())
    print(user.get_price())
    print(user.get_name())
    print(user.get_date())
    print(user.get_date_of_publ())
    print(user.get_name_of_adv())
    print(user.get_phone())
