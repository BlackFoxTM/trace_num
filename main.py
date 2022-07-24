import requests 
from bs4 import BeautifulSoup
import re , json 
from pyfiglet import Figlet
import colorama

cv = colorama.Fore.WHITE
rd = colorama.Fore.RED
bl = colorama.Fore.BLUE
mag = colorama.Fore.MAGENTA
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
gbl = colorama.Fore.LIGHTBLUE_EX

def get_info_phone(koso , operators):
    with requests.Session() as session:
        phone = requests.utils.quote(koso)
        url =f"https://www.phonenumbertrack.com/phone-number-track-trace-result?country=&phone={phone}&submit=#QueryResult"
        req = session.get(url).text
        soup = BeautifulSoup(req , "html.parser")
        kos = soup.find("tbody").text
        koon = soup.find("div" , class_="row panel panel-default details").text
        if "Operator" in kos:
            return (koon.replace("International Call Prefix" , "International Call Prefix : ").replace("Country Code" , "\nCountry Code : +").replace("(ایران)" , " or Iran ").replace("Area Code" , "\nArea Code : ").replace("Subscriber’s Number" , "\nSubscriber’s Number:") + "\n==========================\n" + kos.replace("Query" , "Query : ").replace("Country " , "\nCountry : ").replace("Phone Type" , "\nPhone Type : ").replace("Area Code" , "\nArea Code ").replace("Advertising & Sponsored links","").replace("Location","\nLocation : ").replace("More Options Check Phone Number" , "").replace("Operator" , "\nOperator : "))
        else:
            return (koon.replace("International Call Prefix" , "International Call Prefix : ").replace("Country Code" , "\nCountry Code : +").replace("(ایران)" , " or Iran ").replace("Area Code" , "\nArea Code : ").replace("Subscriber’s Number" , "\nSubscriber’s Number:") + "\n==========================\n" + kos.replace("Query" , "Query : ").replace("Country " , "\nCountry : ").replace("Phone Type" , "\nPhone Type : ").replace("Area Code" , "\nArea Code ").replace("Advertising & Sponsored links","").replace("Location","\nLocation : ") + "\nKnown Provider : %s" % (operators))
def operator(number):
    site = "https://www.celltrack.eu/site/trace"    
    payload = {"_csrf":"J-sER_hYlIW2sj9tpjqyeYmDECR07hsR58zHHm5ILYNGpmIdnHXmvdrXd1n8d8A__9kiYw2bQUag_otXA2Vdsg==","use-alt.flow":"1","TrackForm[phone]":number}
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" , "Cookie" :'lang=en; currentCountry=IR; PHPSESSID=fd20137eacfb20b8da0da15cbd7e95cc; _csrf=582230097b3f6b91512381fafdc543214e99b0fb2d120410461a1105b7fda7c0a:2:{i:0;s:5:"_csrf";i:1;s:32:"aMfZd-r8leH4ZMrFvZ2GyuZWG2LIm-p1";}; _gid=GA1.2.2128828554.1658496315; _gaexp=GAX1.2.R26ZEKfQQy-7-ZdDfEyqnQ.19257.1; _gcl_au=1.1.562173569.1658496316; _gat_UA-114079383-1=1; _ga_81BBDDRXGL=GS1.1.1658496316.1.0.1658496316.0; _ga=GA1.1.346672535.1658496315'}

    req = requests.post(site , headers=headers , data=payload)
    soup = BeautifulSoup(req.text , "html.parser")
    final =  soup.find_all("tbody")[1].find_all("tr")[1].find_all("td")[1].text

    return final.replace(" " , "").replace("\n" , "")

def logo():
    return Figlet(font="slant").renderText("B F S T")

print (gbl + "\t" + logo())
print (gn + "\t Black Fox Security Team" + rd + "\n\t[&] Coded By Maximum Radikali" + mag + "\n\t[-] Channel - > " + bl + "https://t.me/BlackFoxSecurityTeam")

number = input(rd + "[$] Enter your Phone With Country Code\n\t Example : +981234567890\n " + bl + "\n- >  " + gn )


print (yl + get_info_phone(number , operator(number) + cv))
