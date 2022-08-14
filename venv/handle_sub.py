import bs4, requests, re


def init_names_prices(*args):
    # creates the tail for the url from keywords
    space = '%20'
    phrase = args[0]
    for word in range(1, len(args)):
        phrase = phrase + space
        phrase = phrase + args[word]
    
    # creats doc object from searching prisjakt with keywords
    link = f"https://www.prisjakt.nu/search?search={phrase}"
    res = requests.get(link)

    # uses html to get the top 10 result name, sorted by best hits
    pj_search_res = bs4.BeautifulSoup(res.text, 'html.parser')
    pj_item_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .kBBoFI')
    item_name_list = [x.getText() for x in pj_item_list]
    item_name_list = item_name_list[:10]

    # uses html to get the top 10 result prices, sorted by best hits and converted to int
    pj_price_list = pj_search_res.select('.ListUl-sc-xo0c91-0 .PriceContainer-sc-rdha17-0 .duGKvV')
    item_price_list = [x.getText() for x in pj_price_list]
    item_price_list = item_price_list[:10]
    item_price_list = [int(''.join(re.findall(r'\d+', x))) for x in item_price_list]
    
    return item_name_list, item_price_list


class subscribe_prisjakt:
    '''object that searches and gets information from prisjakt
        it will store the information and pick it up again for later search and compairson'''

    def __init__(self) -> None:
        # initial search keywords
        pass

    def get_price_item(item_name):
        # gets item from DB and returns top three results along with names
        space = '%20'
        split_name = item_name.split(' ')
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


    def check_item_result(item_name, item_name_list):
        # takes name from DB and list of top three result name and returns if its 80% valid
        split_name = item_name.split(' ')
        full_hit = len(split_name)
        return_list = []
        for i in item_name_list:
            hit_count = 0
            for j in split_name:
                if j in i:
                    hit_count += 1
            if hit_count / full_hit > 0.8:
                return_list.append(i)
        return return_list


x = 'Asus Radeon RX 6900 XT ROG Strix Gaming LC Topf HDMI 2xDP 16GB'
y_list = ['Asus Radeon RX 6900 XT ROG Strix Gaming LC Top HDMI 2xDP 16GB', 
'Asus Radeon RX 6900 XT ROG Strix Gaming LC OC HDMI 2xDP 16GB', 
'Tomtefar Radeon RX 6700 XT Gaming HDMI 2xDP 12GB']


    # TODO create function that loads data into the database
