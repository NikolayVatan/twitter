import requests
from lxml import html
import collections


def search(username):
    url = 'https://twitter.com/' + username
    r = requests.get(url)
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
        info = tree.xpath("//*[@id='page-container']/div[2]/div/div/div[1]/div/div/div/div[1]/p")
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
        print(img[0].xpath('./@src')[0])
        for i in name:
            print(i.text)
        for b in info:
            print(b.text)
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

        for d in reg:
            print(d.text)
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

        for rc in readercol:
            print(rc.text)
        for fc in followerscol:
            print(fc.text)
        for l in like:
            print(l.text)

        total = {'photo': img[0].xpath('./@src')[0], 'name': i.text, 'info': b.text, 'location': locat, 'site': ste,
                 'date_reg': d.text, 'date_birth': dr, 'gallery': gal, 'col-twits': ct, 'reader': rc.text,
                 'followers': fc.text, 'likes': l.text, 'result': result}
        return collections.OrderedDict(total)


if __name__ == '__main__':
    print(search)