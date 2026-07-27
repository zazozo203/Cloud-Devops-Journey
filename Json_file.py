try:

            import json

            data = '/mnt/c/Users/zazozo/desktop/generat'
            find = input("Enter the user id to find: ")
            fo = open(data, 'r')
            load = json.loads(fo.read()).get('users')


            for user in load:
                    if 'id' in user:
                        if user['id'] == find:
                            print(user)
                            print(4/0)
            fo.close()  
except Exception as e:
    print(e)

 