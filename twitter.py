import requests
import pymongo
from pymongo import MongoClient
import pprint
from lxml import html
import collections


def search(username):
    url = 'https://twitter.com/' + username
    r = requests.get(url)
    client = MongoClient()
    db = client.test_database
    twitter = db.twitter
    user = twitter.find_one({'username': username})
    if 'К сожалению, такой страницы нет!' in r.text:
        result = {
            'exists': False
        }
        return result
    else:
        result = {
            'exists': True,
            'link': url
        }
        tree = html.fromstring(r.text)
        name = tree.xpath("//div[@class='ProfileHeaderCard']/h1/a")
        info = tree.xpath("//div[@class = 'ProfileHeaderCard']/p")
        loc = tree.xpath("//div[@class='ProfileHeaderCard-location ']/span[2]")
        site = tree.xpath("//div[@class='ProfileHeaderCard-url ']/span[2]/a")
        reg = tree.xpath("//div[@class='ProfileHeaderCard-joinDate']/span[2]")
        birth = tree.xpath("//div[@class='ProfileHeaderCard-birthdate ']/span[2]/span")
        img = tree.xpath("//div[@class = 'ProfileAvatar']/a/img")
        media = tree.xpath("//div[@class ='PhotoRail-heading']/span[2]/a[1]")
        twitscol = tree.xpath("//div[@class='ProfileNav']/ul/li[1]/a/span[3]")
        readercol = tree.xpath("//div[@class='ProfileNav']/ul/li[2]/a/span[3]")
        followerscol = tree.xpath("//div[@class='ProfileNav']/ul/li[3]/a/span[3]")
        like = tree.xpath("//div[@class='ProfileNav']/ul/li[4]/a/span[3]")
        name = name[0].text
        info = info[0].text
        reg = reg[0].text
        readercol = readercol[0].text
        followerscol = followerscol[0].text
        like = like[0].text
        locat = ''
        for mesto in loc:
            if mesto.text is None:
                continue
            txt = mesto.text
            locat += txt.strip() + ' '

        ste = ''
        for a in site:
            if a.text is None:
                continue
            txt = a.text
            ste += txt.strip() + ' '

        dr = ''
        for n in birth:
            if n.text is None:
                continue
            txt = n.text
            dr += txt.strip() + ' '

        gal = ''
        for m in media:
            if m.text is None:
                continue
            txt = m.text
            gal += txt.strip() + ' '

            ct = ''
        for s in twitscol:
            if s.text is None:
                continue
            txt = s.text
            ct += txt.strip() + ' '

        total = {'photo': img[0].xpath('./@src')[0], 'name': name, 'info': info, 'location': locat, 'site': ste,
                 'date_reg': reg, 'date_birth': dr, 'gallery': gal, 'col-twits': ct, 'reader': readercol,
                 'followers': followerscol, 'likes': like, 'result': result, 'user': user}
        return collections.OrderedDict(total)


if __name__ == '__main__':
    print(search)
