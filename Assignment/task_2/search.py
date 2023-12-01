import requests
import sys
sys.path.append('../')
import os 

from utils.utils import *
from requests.structures import CaseInsensitiveDict


def perform_curl_request(product, start, count):
    url = "https://search.cisco.com/services/search"

    headers = CaseInsensitiveDict()
    headers['authority'] = 'search.cisco.com' 
    headers['accept'] = 'application/json, text/plain, */*' 
    headers['accept-language'] = 'en-IN,en-GB;q=0.9,en;q=0.8' 
    headers['content-type'] = 'application/json' 
    headers['cookie'] = "CP_GUTC=49.44.217.36.3137591170115489459; UnicaNIODID=undefined;_biz_uid=4562446067b04b6ad3f911b9f7f68936; _gcl_au=1.1.1517360827.1701154896; _biz_flagsA=%7B%22Version%22%3A1%2C%22Ecid%22%3A%221423303062%22%2C%22XDomain%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%7D; AMCVS_B8D07FF4520E94C10A490D4C%40AdobeOrg=1; aam_uuid=36611535424635042025921182215769300986; ORA_FPC=id=df2c0957-36b4-4813-b1ce-ef44ad6044a1; ELOQUA=GUID=0D1FCC301AD14E83A336CF86BA33BF63; _fbp=fb.1.1701154908123.1922494182; check=true; OptanonAlertBoxClosed=2023-11-28T07:01:56.905Z; _cs_c=0; aam_uuid=36611535424635042025921182215769300986; _rdt_uuid=1701158444169.8f7dddaf-f291-459c-8ceb-747cedf6fbdc; _ga_YRQD6F0TMK=GS1.2.1701158455.1.0.1701158455.60.0.0; _ga_DLWJ5W23ER=GS1.1.1701158445.1.1.1701158478.0.0.0; _gid=GA1.2.227519227.1701358045; _abck=73C750FED1235CDFA5C167A81D0B299D~-1~YAAQtvhWuBt8RemLAQAA6UexJArSzlq+c6gsAx5+fOVo0TwmlTq4aHMkNKF4hl+rsgEglg1oYqFPjs4nyaZqqTh6KvAW6/NO7QoKjkY7A2w6U1qm2s84njfxtUVOApzBWoDfwmYuhEFQkebuQECypxPIcJK20YhnYu1TF9zlitGX8aum9mppuN6f0eoyt3d/HfRvVzbM7OTmZ+7MTw1bE6Po7Do9utM5+NIGHkjgiDfR+p4OFh1YbMJIPvd6Wojmc0Fwlv7biFluinMZvCPpZp+zJEbG1lZTRY1N4T9jCWJUBP1zZTq1T5GRGbYEfc+ms5Q/n0R+MYALo61+S8Tfx2o+hXlNLSIHw0NGfhhXMcjcZ8yjjJAKzmifWyYdcnrG2i9KoEDM2/i7~-1~-1~-1; bm_sz=378D8B7396D8AB87641E25716FABB4FC~YAAQtvhWuBx8RemLAQAA6UexJBWE8mus14dLtLIYBp7XEB+39psWxW3eNbZYSSWRiGFmSxYVy+5kMNBFVw9sQvcyLo049FAIgAVTU4bpMUcWDP6lVO5++LTfnjC1cvLf3z4YWHITnb5nCvANOkQpKlUxVUFLR4L02QXolANnuGslqGj9UTuaJw9NK4k4AqkjyVRlrldZ4rYRAFtZwARxpgU/TYfbElx/UjvIAnFfckMQ9vN4yfQ2JybaUcdgefuSrn8y3ibk+7RAOkjr0J5N6QBC1KGqfOjACUruPBvM7o6KkA==~3556408~3753525; _cs_cvars=%7B%222%22%3A%5B%22Template%20Name%22%2C%22marketing%22%5D%2C%223%22%3A%5B%22Title%22%2C%22Cisco%20Line%20Cards%22%5D%2C%225%22%3A%5B%22Page%20Name%22%2C%22search.cisco.com%22%5D%2C%226%22%3A%5B%22Content%20Type%22%2C%22no%20contenttype%22%5D%7D; WTPERSIST=cisco.aam_uuid=36611535424635042025921182215769300986&cisco._ga=GA1.1.1625462272.1701154896&cisco.eloqua_guid=0d1fcc301ad14e83a336cf86ba33bf63&cisco.utag_main_v_id=018c14bbb668001494c6ba5d6fb305075003706d00998; _biz_nA=54; _uetsid=f42ddde08f9411ee958c39717a0934ac; _uetvid=ff9040a08dbb11ee9ebaf106ac39e00b; _biz_pendingA=%5B%5D; s_ptc=%5B%5BB%5D%5D; s_cc=true; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+01+2023+17%3A21%3A45+GMT%2B0530+(India+Standard+Time)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=403949cd-c1de-45af-91c4-0a1c48ee678d&interactionCount=2&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=IN%3BMH; JSESSIONID=E44A07D40FB44999781DEF539B59D18D; gpv_v9=search.cisco.com%2Fsearch; s_ppvl=search.cisco.com%2Fsearch%2C78%2C78%2C799%2C1470%2C799%2C1470%2C956%2C2%2CP; _ga=GA1.1.1625462272.1701154896; _cs_id=bf09809b-5e44-a95c-c77c-deedad3d78b1.1701155041.7.1701431508.1701431508.1589297132.1735319041026; _cs_s=1.5.0.1701433309026; ADRUM=s=1701431687213&r=https%3A%2F%2Fsearch.cisco.com%2Fsearch%3Fhash%3D-165683481; mbox=session#0cf275264ebe4c5ea49885c8833a699f#1701433594; utag_main=v_id:018c14bbb668001494c6ba5d6fb305075003706d00998$_sn:6$_se:112$_ss:0$_st:1701433546900$vapi_domain:cisco.com$ses_id:1701429709488%3Bexp-session$_pn:13%3Bexp-session$ctm_ss:true%3Bexp-session; _ga_KP8QEFW4ML=GS1.1.1701429710.8.1.1701431747.60.0.0; s_ppv=search.cisco.com%2Fsearch%2C94%2C94%2C799%2C588%2C799%2C1470%2C956%2C2%2CL; AMCV_B8D07FF4520E94C10A490D4C%40AdobeOrg=281789898%7CMCIDTS%7C19692%7CMCMID%7C42735286330627949556606177863229113979%7CMCAID%7CNONE%7CMCOPTOUT-1701438958s%7CNONE%7CvVersion%7C4.1.0"
    headers['origin'] = 'https://search.cisco.com' 
    headers['referer'] = "https://search.cisco.com/search?locale=enUS&query=cisco%20switches&bizcontext=&mode=text&clktyp=enter&autosuggest=false"
    headers['sec-ch-ua'] = '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' 
    headers['sec-ch-ua-mobile'] = '?0' 
    headers['sec-ch-ua-platform'] = '"macOS"' 
    headers['sec-fetch-dest'] = 'empty' 
    headers['sec-fetch-mode'] = 'cors' 
    headers['sec-fetch-site'] = 'same-origin' 
    headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/119.0.0.0 Safari/537.36'

    data = '{"query":"' + product + '","startIndex":' + str(start) + ',"count":' + str(count) + ',"searchType":"CISCO","tabName":"Cisco","debugScoreExplain":false,"facets":[],"sortType":"RELEVANCY","dynamicRelevancyId":"","categoryValue":"","breakpoint":"XS","searchProfile":"","ui":"one","searchCat":"","searchMode":"text","callId":"XH5swmEqHr","requestId":1701431852702,"taReqId":"","bizCtxt":"","qnaTopic":[],"appName":"CDCSearchFE","social":false,"localeStr":"enUS","onlyOrganic":false,"ppscountry":"","ppslanguage":"","ppsjobrole":false,"pq":"","pq_cat":"","additionalParams":""}'

    resp = requests.post(url, headers=headers, data=data)

    return resp


def create_document(item):
    document = ''

    if item['title'] is not None:
        document += item['title'] + '\n\n'
    
    if item['description'] is not None:
        document += item['description'] + '\n\n'
    
    if item['content'] is not None:
        for c in item['content']:
            document += c + '\n'

        document += '\n'
    
    if item['concept'] is not None:
        document += item['concept'] + '\n\n'

    return document


def create_directory(name):
    path = 'products/' + name

    try:
        os.mkdir(path)
    except OSError as error:
        print(error)


def main():
    # Extract products from categories_products
    filename = '../task_1/categories_products.json'
    f = open(filename)
    cat_prods = json.load(f)

    products = get_products(cat_prods)
    # write_list_to_file('products.txt', products)

    NUM_DOCS = 1000

    for query in products:
        ctr = 1
        START = 0
        COUNT = 50
        dir_name = ''.join([c for c in query if c.isalnum() or c == ' '])
        dir_name = dir_name.lower().replace(' ', '_') + '/'
                    
        while (START+COUNT) <= NUM_DOCS:
            print(f"Product: {query}, Start: {START}")
            resp = perform_curl_request(query, START, COUNT)
            
            if resp.status_code == 200:
                response = json.loads(resp.text)

                for item in response['items']:
                    document = create_document(item)
                    
                    if ctr == 1:
                        create_directory(dir_name)

                    filename = 'products/' + dir_name + str(ctr) + '.txt'
                    write_text_to_file(filename, document)

                    ctr += 1
            START += COUNT


if __name__=='__main__':
    main()
