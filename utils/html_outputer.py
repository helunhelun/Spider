#coding:utf-8

class HtmlOutputer(object):
    """
    HTML DATA OUTPUT
    """
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        """
        LET ALL DATA STORAGE IN A LIST OBJECT OF DATA
        :param data: A DATA
        :return: NONE
        """
        if data is None :
            return
        self.datas.append(data)


    def output_html(self):
        """
        LET ALL DATA OUTPUT WITH A HTML FORMAT
        :return: NONE
        """
        with open('output.html', 'w') as f :
            f.write("<html>")
            f.write("<head>")
            f.write("<meta charset='UTF-8'>")
            f.write("<title>")
            f.write("Spider baike output")
            f.write("</title>")
            f.write("</head>")
            f.write("<body>")
            f.write("<table>")
            f.write("<td>url链接网站</td>")
            f.write("<td>标题</td>")
            f.write("<td>概要</td>")
            for data in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>" % data['url'])
                f.write("<td>%s</td>" % data['title'])
                f.write("<td>%s</td>" % data['summary'])
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")