from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json


URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.57120616308593%2C%22east%22%3A-80.11664683691406%2C%22south%22%3A25.527796614239158%2C%22north%22%3A25.877983112236798%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22],%22cat2%22:[%22total%22]}&requestId=8'

def cookie_parser():
    cookie_string = 'x-amz-continuous-deployment-state=AYABeMypiKCslu3G4AN59HyHbdgAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzlQQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADEsaim0y3qC%2FOIO4xAAwbYE2jyTzIY6Zq1nOrCupuq%2Fv5NnY2d2GljpzgMi0NBw2vXz8huwg8GXS7ObfOl+IAgAAAAAMAAQAAAAAAAAAAAAAAAAAAH8p0NzFBJQAM1UPCl0alX3%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAylT798VSTVxfAr+NIsuawYl5A4qZMWAdZegoAVA4qZMWAdZegoAQ==; zguid=24|%24c4e3aab6-00f3-4057-adab-cadd34221369; zgsession=1|c88c6e53-744a-4d90-8a60-cd68dc88135a; JSESSIONID=E79773D67A7F8F2C8C1AF7EA11020398; AWSALB=VPGFv44nlXf9hXmOucHu5YbXVibjrW9895fJOhEGvxdKuURU9qRBDulb7w58sChNigyRs9yLBrZESGLHWFZc8b927DPCHkJrYKqo+9HBtNptmnL6O/KSlpDHp6SX; AWSALBCORS=VPGFv44nlXf9hXmOucHu5YbXVibjrW9895fJOhEGvxdKuURU9qRBDulb7w58sChNigyRs9yLBrZESGLHWFZc8b927DPCHkJrYKqo+9HBtNptmnL6O/KSlpDHp6SX; search=6|1679818192516%7Crect%3D25.877983112236798%252C-80.11664683691406%252C25.527796614239158%252C-80.57120616308593%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D3%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0912700%09%09%09%09%09%09'
    
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    
    return cookies

def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    
    search_query_state = query_string.get('searchQueryState')
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f'https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}'
    
    return new_url
    