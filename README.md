# amazondt

```
fromstring(html, base_url=None, parser=None, **kw)
source code
Parse the html, returning a single element/document.

fromstring() 可以在解析xml格式时，将字符串转换为Element对象，解析树的根节点。
在python中，对返回的page.txt做fromstring()处理，可以方便进行后续的xpath定位等。
如：
page = requests.get(url)
data = html.fromstring(page.txt)
getData = data.xpath('........')
```

```
from itertools import cycle
cycle()会把传入的一个序列无限重复下去
```
