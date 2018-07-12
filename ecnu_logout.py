import requests
import sys

#登录地址
post_addr="https://login.ecnu.edu.cn/include/auth_action.php"

#构造头部信息
post_header={
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		'Content-Length': '107',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': 'login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYpuUxcq5od7dlmpltnEal5DQ0gjD6r1n3%252Fhz5Ndv3l%252FxDuNn8jsHuEDCr2BFRDfRYRw2lSpGv8mAsB%252FTG6xFGqlgUw0Xjk65OPxQNFGhLmZ24drwZxp8kv8nzffCTVZo9pEs7xzVqNwVNbU64ooymQU%253D; _ga=GA1.3.908443897.1522253864; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcroYpuUxcq5od7dlmpltnEal5DQ0gjD6r1n3%252Fhz5Ndv3l%252FxDuNn8jsHuEDCr2BFRDfRYRw2lSpGv8mAsB%252FTG6xFGqlgUw0Xjk65OPxQNFGhLmZ24drwZxp8kv8nzffCTVZo9pEs7xzVqNwVNbU64ooymQU%253D',
		'Host': 'login.ecnu.edu.cn',
		'Origin': 'https://login.ecnu.edu.cn',
		'Referer': 'https://login.ecnu.edu.cn/srun_portal_pc.php?ac_id=1&',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest'
}

post_data = {
		'action': 'logout',
		'username': sys.argv[1],
		'password': sys.argv[2],
		'ajax': '1'
	}
response =requests.post(post_addr,data=post_data,headers=post_header)
info = "###########################################################################################################\n" \
       "##由于学校上网认证设计的脑残性，无论登出与否，均返回200 ok，故我无法判断登出状态。请你 ping www.baidu.com自行验证是否登出成功##\n" \
       "###########################################################################################################"
print(info)