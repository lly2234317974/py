#conding:utf-8
#数据的处理

import re
#取出特殊字符串
def strip_symbol(string):
    '''
    string:要处理的字符串
    return:处理之后的字符串


    :param string:
    :return:
    '''
    pattern=re.compile('\r|\n|\t|',re.S)
    string=re.sub(pattern,'',string)
    return string


#去除文本中的标签
def strip_ele(string):
    pattern=re.compile('<.*?>')
    string=re.sub(pattern,'',string)
    return string



def replace_br(string):
    pattern=re.compile('<br>|<br\>',re.S)
    string=re.sub(pattern,'',string)
    return string















