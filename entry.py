from rest import RestManager
import json
import argparse
import os

db_home = 'http://localhost:3000/api/dashboards/home'
db_uid = 'http://localhost:3000/api/dashboards/uid'
db = 'http://localhost:3000/api/dashboards/db'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method', default='post', help='action to take')
    parser.add_argument('-d', '--data', default='create', help='file to adopt')
    args = parser.parse_args()

    data = None
    if args.method == 'post':
        url = db
        with open('./templates/{}.json'.format(args.data)) as fd:
            data = json.load(fd)
    elif args.method == 'get':
        url = os.path.join(db_uid, args.data)
    elif 'del' in args.method:
        url = os.path.join(db_uid, args.data)
        args.method = 'delete'
    else:
        print 'Not Supported Method'

    # print json.dumps(RestManager().post(url=url, data=data))
    print json.dumps(eval('RestManager().{}(url=url, data=data)'.format(args.method)))
