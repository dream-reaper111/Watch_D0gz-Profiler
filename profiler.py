import os
import threading
from lxml import html
import requests
from time import sleep
import grab_proxy
import sys

header = {
'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Connection': 'Close'
}
httpp, httpo, httpsp, httpspo = grab_proxy.getProxies()
prox = {
    "http": "http://" + httpsp[0].strip("\n") + ":" + httpspo[0].strip("\n"),
    "https": "http://" + httpp[0].strip("\n") + ":" + httpo[0].strip("\n")
}
def scrape1(proxi, ind, l, f, loc, mx):
    sleep(10)
    shitty = False
    try:
        open = requests.get("http://www.peekyou.com/"+l.lower()+"_"+f.lower(), headers=header, stream=False, proxies=proxi)
        code = html.fromstring(open.content)
        print open.content
        open.close()
        maininfo = code.xpath('//p[@class="user_line1"]/text()')
        extrainfo = code.xpath('//p[@class="user_line3"]/text()')
        if len(maininfo):
            counter = 0
            for n in maininfo:
                print "_____________________________________________________________________________________________________"
                print "Main Info:"
                print n
                if (len(extrainfo)-counter) > 0:
                    print "Extra Info:"
                    print extrainfo[counter]
                print "_____________________________________________________________________________________________________"
                counter+=1
    finally:
        if shitty:
            return
        elif mx <= 0:
            print "\nCan't find anything here..."
            return
        print "\nSomething went wrong! Migrating proxies for scraper #2..."
        ind += 1
        mx -= 1
        proxi = {
            "http": "http://" + httpsp[ind].strip("\n") + ":" + httpspo[ind].strip("\n"),
            "https": "http://" + httpp[ind].strip("\n") + ":" + httpo[ind].strip("\n")
        }
        scrape1(proxi, ind, l, f, loc, mx)


def scrape3(proxi, ind, l, f, loc, mx):
    sleep(10)
    try:
        if loc == "nada":
            open = requests.get("https://thatsthem.com/name/" + l + "-" + f, headers=header, stream=False, proxies=proxi)
        else:
            open = requests.get("https://thatsthem.com/name/" + l + "-" + f + "/"+ loc.upper(), headers=header, stream=False, proxies=proxi)
        code = html.fromstring(open.content)
        open.close()
        name = code.cssselect(".full-name.mb0")
        age = code.xpath("//div[@class='mt0']/text()")
        phone = code.xpath("//span[@itemprop='telephone']/text()")
        location = code.xpath("//span[@itemprop='addressLocality']/text()")
        location2 = code.xpath("//span[@itemprop='streetAddress']/text()")
        location3 = code.xpath("//span[@itemprop='addressRegion']/text()")
        location4 = code.xpath("//span[@itemprop='postalCode']/text()")
        #occupat = code.xpath("//ul[@class='list-unstyled list-inline record-list']/text()")
        #occupat = code.cssselect(".list-unstyled.list-inline.record-list")
        print "\n_________________________________________________________________________________________________________"
        print "Results #3"
        print "_________________________________________________________________________________________________________"
        counter = 0
        if len(name):
            for n in name:
                print "Name:"
                print " ".join(n.text_content().split())
                if (len(age)-(counter+5)) > 0:
                    print "".join(age[counter+5].strip())
                if (len(location)-counter) > 0:
                    print "Location:"
                    print location2[counter],location[counter], location3[counter],location4[counter]
                if (len(phone)-counter) > 0:
                    print "Phone:"
                    print phone[counter]
                #if (len(occupat)-counter) > 0:
                #    print "Occupation:"
                #    print " ".join(occupat[counter].text_content().split())
                print "_____________________________________________________________________________________________________"
                print "\n"
                counter+=1
        else:
            print "\nCan't find anything here..."
            return
    except:
        if mx <= 0:
            print "\nCan't find anything here..."
            return
        print "Something went wrong! Migrating proxies..."
        ind += 1
        mx -= 1
        proxi = {
            "http": "http://" + httpsp[ind].strip("\n") + ":" + httpspo[ind].strip("\n"),
            "https": "http://" + httpp[ind].strip("\n") + ":" + httpo[ind].strip("\n")
        }
        scrape3(proxi, ind, l, f, loc, mx)
def scrape2(proxi, ind, l, f, loc, mx):
    sleep(7)
    shitty = False
    try:
        if loc == "nada":
            open = requests.get("http://www.zabasearch.com/people/"+l.lower()+"+"+f.lower()+"/", headers=header, stream=False, proxies=proxi, allow_redirects=True)
        else:
            open = requests.get("http://www.zabasearch.com/people/"+l.lower()+"+"+f.lower()+"/"+loc.lower()+"/", headers=header, stream=False, proxies=proxi, allow_redirects=True)
        code = html.fromstring(open.content)
        open.close()
        name = code.xpath('//span[@itemprop="name"]/text()')
        address = code.xpath('//font[@itemprop="streetAddress"]/text()') + code.xpath('//span[@itemprop="addressLocality"]/text()') + code.xpath('//span[@itemprop="addressRegion"]/text()') + code.xpath('//font[@itemprop="postalCode"]/text()')
        phone = code.xpath('//span[@itemprop="telephone"]/text()')
        if len(name):
            shitty = True
            counter = 0
            print "\n_________________________________________________________________________________________________________"
            print "Results #2"
            print "_________________________________________________________________________________________________________"
            for n in name:
                print "_________________________________________________________________________________________________"
                print "Name:"
                print n
                if (len(address) - counter) > 0:
                    print "Location:"
                    print address[counter]+address[counter+3]+", "+address[counter+6]+" "+address[counter+9]
                if (len(phone) - counter) > 0:
                    print "Phone:"
                    print phone[counter]
                print "_________________________________________________________________________________________________"
                counter+=1
        elif len(address):
            shitty = True
            print "\n_________________________________________________________________________________________________________"
            print "Results #2"
            print "_________________________________________________________________________________________________________"
            print "\n"
            print "_________________________________________________________________________________________________"
            print "Name:"
            print code.xpath('//font[@itemprop="name"]/text()')[0]
            print "Location:"
            print code.xpath('//span[@itemprop="streetAddress"]/text()')[0] + " " + code.xpath('//span[@itemprop="addressLocality"]/text()')[0] + ", " + code.xpath('//span[@itemprop="addressRegion"]/text()')[0] + " " + code.xpath('//font[@itemprop="postalCode"]/text()')[0]
            print "Phone:"
            print code.xpath('//font[@itemprop="telephone"]/text()')[0]
            print "_________________________________________________________________________________________________"

    finally:
        if shitty:
            return
        elif mx <= 0:
            print "\nCan't find anything here..."
            return
        print "\nSomething went wrong! Migrating proxies for scraper #2..."
        ind += 1
        mx -= 1
        proxi = {
            "http": "http://" + httpsp[ind].strip("\n") + ":" + httpspo[ind].strip("\n"),
            "https": "http://" + httpp[ind].strip("\n") + ":" + httpo[ind].strip("\n")
        }
        scrape2(proxi, ind, l, f, loc, mx)

def searchall(ind, l,f,loc="nada"):
    #temp = threading.Thread(target=scrape1, args=[prox, ind, l,f,loc,2])
    temp2 = threading.Thread(target=scrape2, args=[prox,ind,l,f,loc,2])
    temp3 = threading.Thread(target=scrape3, args=[prox, ind, l,f,loc,2])
    #temp.start()
    temp2.start()
    temp3.start()

def main():
    try:
        while 1:
            print "----------------------------------------------------------------------------------------------------"
            inp = raw_input("Name of person: ")
            stringtest = inp
            if inp == "migrate":
                indx += 1
                prox = {
                    "http": "http://" + httpsp[indx].strip("\n") + ":" + httpspo[indx].strip("\n"),
                    "https": "http://" + httpp[indx].strip("\n") + ":" + httpo[indx].strip("\n")
                }
                print prox
            else:
                f = stringtest[stringtest.index(" ") + 1:]
                l = stringtest[:stringtest.index(" ")]
                inp = raw_input("State (Leave blank if none): ")
                loc = inp
                if loc == "":
                    loc = "nada"
                searchall(0, l, f, loc)
                sleep(1)
                a = raw_input("Press enter to search new person")
                del a
                os.system("clear")
    except KeyboardInterrupt:
        print "\nExiting profiler..."
        sys.exit(0)

main()

