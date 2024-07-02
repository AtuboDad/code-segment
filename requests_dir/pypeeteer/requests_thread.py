# -*- coding: utf-8 -*-
import requests
import logging
from lxml import etree
from Commons import status_codes, progress_infos

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
           'Accept': '*/*'}


def do_start(start_params):
    response = requests.get(start_params.start_url, data=None, headers=headers)
    if response and response.status_code == requests.codes.ok:
        logging.info('请求成功')
        # print(response.content.decode("GBK"))
        bs = etree.HTML(response.content.decode("GBK"))
        # bs = etree.HTML('<html><body><div class="co_content8"><ul><li><a>haha</a></li><li><a>haha2</a></li></ul></div></body></html')
        items = bs.xpath('//div[@class="co_content8"]/ul/td/table')
        for item in items:
            title = '|'.join(item.xpath('./tr[2]/td[2]/b/a/text()'))
            print(title)
            date = item.xpath('./tr[3]/td[2]/font/text()')[0]
            print(date)
            description = item.xpath('./tr[4]/td[1]/text()')[0]
            print(description)
            print('================================================')
    return {'status': 'success', 'msg': '成功'}


# if __name__ == '__main__':
#     str_a = b'<html><body><div class="co_content8"><ul><table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">&#13;\n<tr> &#13;\n<td height="1" colspan="2" background="/templets/img/dot_hor.gif"></td>&#13;\n</tr>&#13;\n<tr> &#13;\n<td width="5%" height="26" align="center"><img src="/templets/img/item.gif" width="18" height="17" /></td>&#13;\n<td height="26">&#13;\n\t<b>&#13;\n\t\t<a class="ulink" href="/html/gndy/dyzz/">[&#31934;&#21697;&#30005;&#24433;]</a>&#13;\n\t\t<a href="/html/gndy/dyzz/20201122/114034.html" class="ulink" title="2020&#24180;&#38889;&#22269;7.3&#20998;&#24778;&#24730;&#29359;&#32618;&#29255;&#12298;&#26080;&#22768;&#12299;BD&#38889;&#35821;&#20013;&#23383;">2020&#24180;&#38889;&#22269;7.3&#20998;&#24778;&#24730;&#29359;&#32618;&#29255;&#12298;&#26080;&#22768;&#12299;BD&#38889;&#35821;&#20013;&#23383;</a>&#13;\n\t</b>&#13;\n</td>&#13;\n</tr>&#13;\n<tr> &#13;\n<td height="20" style="padding-left:3px">&#160;</td>&#13;\n<td style="padding-left:3px">&#13;\n\t\t\t\t<font color="#8F8C89">&#26085;&#26399;&#65306;2020-11-22 &#13;\n&#28857;&#20987;&#65306;0 </font>&#13;\n\t\t&#13;\n\t\t\t\t</td>&#13;\n</tr>&#13;\n<tr> &#13;\n<td colspan="2" style="padding-left:3px">&#9678;&#35793;&#12288;&#12288;&#21517;&#12288;&#25910;&#23608;&#20154;(&#21488;)/&#36830;&#22768;&#38899;&#37117;&#27809;&#26377;(&#21488;)/&#26080;&#22768;&#26080;&#24687;/Voice of Silence\n&#9678;&#29255;&#12288;&#12288;&#21517;&#12288;&amp;#49548;&amp;#47532;&amp;#46020; &amp;#50630;&amp;#51060;\n&#9678;&#24180;&#12288;&#12288;&#20195;&#12288;2020\n&#9678;&#20135;&#12288;&#12288;&#22320;&#12288;&#38889;&#22269;\n&#9678;&#31867;&#12288;&#12288;&#21035;&#12288;&#24778;&#24730;/&#29359;&#32618;\n&#9678;&#35821;&#12288;&#12288;&#35328;&#12288;&#38889;&#35821;\n&#9678;&#23383;&#12288;&#12288;&#24149;&#12288;&#20013;&#25991;&#23383;&#24149;\n&#9678;&#19978;&#26144;&#26085;&#26399;&#12288;2020-10-15(&#38889;&#22269;)\n&#9678;&#35910;&#29923;&#35780;&#20998;&#12288;7.3/10 from 12666 users\n&#9678;IMDb&#35780;&#20998;&#12288;6.9/10 from 98 users\n&#9678;&#25991;&#20214;&#26684;&#24335;&#12288;x264 + ACC\n&#9678;</td>&#13;\n</tr>&#13;\n</table>\n</ul></div></body></html'
#     bs = etree.HTML(str_a.decode("GBK"))
#     items = bs.xpath('//div[@class="co_content8"]/ul/table')
#     for item in items:
#         print(item.xpath('./tr[2]/td[2]/b/a/text()'))