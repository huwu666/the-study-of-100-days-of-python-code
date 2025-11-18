status_code = int(input('响应码'))
if status_code == 400:
    description = 'bad request'
elif status_code == 401:
    description = 'unauthorized'
elif status_code == 403:
    description = 'forbidden'
elif status_code == 404:
    description = 'not found'
elif status_code == 405:
    description = 'method not allowed'
elif status_code == 418:
    description = 'i am a teapot'
elif status_code == 429:
    description = 'too many requests'
else:
    description = 'unknown status code'
print('状态码描述: ' , description)