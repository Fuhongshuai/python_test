import requests
import sys


def solve(username,projectname,id):
    #print(str(username))
    #print(str(projectname))
    response = requests.get('https://api.github.com/repos/'+str(username)+'/'+str(projectname)+'/issues/'+str(id))
    # 检测是否请求成功，若成功，状态码应该是200
    if (response.status_code != 200):
        print('error: fail to request')

    # 获取的是一个json格式的字典对象
    j = response.json()
    print(j['title'])


if __name__ == '__main__':
    #for i in range(1, len(sys.argv)):
    #    print(sys.argv[i])
    solve(sys.argv[1],sys.argv[2],sys.argv[3])
