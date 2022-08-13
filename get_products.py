import bs4, requests, re


class search_prisjakt:
    '''object that searches and gets information from prisjakt
        it will store the information and pick it up again for later search and compairson'''

    def __init__(self, item, *args) -> None:
        # initial search keywords
        self.args = args
        self.item = item

    def create_link(args):
        # creates the tail for the url from keywords
        space = '%20'
        phrase = args[0]
        for word in range(1, len(args)):
            phrase = phrase + space
            phrase = phrase + args[word]
        return phrase

    def get_names_prices(args):
        # searches for the keywords and returns two lists - names and prices
        link = f"https://www.prisjakt.nu/search?search={create_link(args)}"
        res = requests.get(link)
        pj_search_res = bs4.BeautifulSoup(res.text, 'html.parser')
        pj_item_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .kBBoFI')
        item_name_list = [x.getText() for x in pj_item_list]
        item_name_list = item_name_list[:10]

        pj_price_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .PriceContainer-sc-rdha17-0 .duGKvV')
        item_price_list = [x.getText() for x in pj_price_list]
        item_price_list = item_price_list[:10]
        item_price_list = [int(''.join(re.findall(r'\d+', x))) for x in item_price_list]
        
        return item_name_list, item_price_list

    def get_price_item(item):
        # gets item from DB and returns top three results along with names
        # TODO make the function filter out results if top three is not like the name loaded into it
        space = '%20'
        split_name = item.split(' ')
        search_phrase = space.join(split_name)
        link = f"https://www.prisjakt.nu/search?search={create_link(search_phrase)}"
        res = requests.get(link)
        pj_search_res = bs4.BeautifulSoup(res.text, 'html.parser')
        pj_item_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .kBBoFI')
        item_name_list = [x.getText() for x in pj_item_list]
        item_name_list = item_name_list[:3]

        pj_price_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .PriceContainer-sc-rdha17-0 .duGKvV')
        item_price_list = [x.getText() for x in pj_price_list]
        item_price_list = item_price_list[:3]
        item_price_list = [int(''.join(re.findall(r'\d+', x))) for x in item_price_list]

        return item_name_list, item_price_list

    # TODO create function that loads data into the database