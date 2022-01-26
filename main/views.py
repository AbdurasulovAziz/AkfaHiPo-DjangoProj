from django.shortcuts import render
# Create your views here.
import schedule
import time
import gspread

credentials = {
  "type": "service_account",
  "project_id": "akfaproject-334606",
  "private_key_id": "36ae32e82ca4720c274ffa19aa1667a90c974400",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0pnzrW1JN+/HF\nIwABFtr4hGYcmO1eo83QWs2iaZ3jVldfPDO4Eayen/KQkKQt8B6oOYwLJq0CmTkA\nxSziB4aUfw16CaQp5LRI88z7KvnFwQSxoiGm1Dw+eJb/6puZhcjfZlXly0r0Uaql\nuWFCksllzg+HWt1qAofurPH+WiIKkjtGXw8indHkb/TSLo3OhcuaywKe/pC+wTni\nVKaThiRCTQPmnc1hTpX4qKVf2s82bRCh7uiLHD2BH1rNy4had+BEwyeR+SQR+5UE\n6MK8ybHkjha6r6kySkIYbxBI74quu7UfgbNt93X1upjNELRVmnr7HAGojElCQ3X4\nVAlGdCpLAgMBAAECggEAUeYOySbYK/m2VMD23geOE0/2+S0NpDPP+Y9JHcITLf81\nUjw5WFBO+YUbE5Y3kIoFZA/e4SlSE1UCxkod/IUb6tOk+PhJACMq5s381rvXi+Nj\nbOLLrdYXT90c2/3xOAsyk7FR7QGaxCQIIOTn5qYkfy6J1LwJmGd4V+j5Nu6G81Iu\nTMNDdpLzzYfhEbE4nbghfY9oX/f8uPEYL2d0pQ+DS+Lo+gZMimAI+Ahvmg5TfbSF\nrZgGLm5JBKxfQJ6NncO5P3Plf93p+15i+dfVjSZ8IO3EL4yFfDd2nvSkJIEzqMSn\nE/3/yTCEMFBKhn+iCNcu47fKRfc777nRIQl7e9gLEQKBgQD5Bb85Vx+e4BMf+44c\nXlWAJgU6Phm1lhOPDidmFxQ7j0ARt1BWkOeEJaF2bHpNZuj12WnBkxGqYl2tqbAL\n28JQwKC9UI1S+jNgM6JgxZFe0b409hVRwxJs2bgQWcuRt6zy/BgurNdDSV+8d8L7\nngXWZCki/6MOI1DXiQfbQ6A0uwKBgQC5tk3DkrM3PTcKOCnxJMX2/oiQs6QI6nH5\nJU0ivRLbO7Fni+caarWYOkxaYFnUQR7Tm7SgBKfcAlmTfZ9nCbPkrVTeGjAliarv\nJAJeC6PcXVjpsBcbpzt/C4PiIj+xlrrw/NUfsYYHisTpADaI+891miKZZ6tPv5cT\n0Hy9i55PsQKBgByatGR5xYASbR/3XVOU4m1d8KvIBlv9aTG9hnkLnZ9ZzRo73FaV\nPoLHb8ySmVnawFe9KZC6vAS+V9Ri8X3rOF7eQZh9cD5fzxb112kWSKSDoz2iJsDF\nj5BBUgtOxTtvxcYDfyOdZvyrqPuVJiiQ9kqyJqeGhcxR8i9P5j8hfX2RAoGAMFQn\n8pBXwTVWAHvTNmUKe5eLtJR7SLKyTFMPus2XfaQQK9E1qCNC9MWfHxnZ5qm3uvvX\nSplLka6u3vofJHJa9VTCNDZ+dxZXfHpTf2PqFavZOp9PtCuWCR7XCF8/UhjWt2Yk\nlGXfalELo1Mh3g4h1AnznRZkd5F1YHuuKqmN3lECgYEA30I5sozPlMyh2QNzNlZv\nv9I8sUc3oolfRWT4XHDbIaqi5/SZLkRMzyfBoSWXFnPlFW3RQm79qP7/7y2rZi5k\n3B04FLl+dNUNrsdLoIC0Ltn0npDDmMoIEb/e88TNFmlQeDpKfSGBzrLN4gBFS1fJ\nFkZgqhorDC9U/liFkFTTS+o=\n-----END PRIVATE KEY-----\n",
  "client_email": "service-account@akfaproject-334606.iam.gserviceaccount.com",
  "client_id": "101814985191203920318",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-account%40akfaproject-334606.iam.gserviceaccount.com"
}

sa = gspread.service_account_from_dict(credentials) # Путь к json файлу данных
sh = sa.open("HiPoAkfa") # Название изменяемого файла
worksheet = sh.worksheet('hipolist') 


def mainPage(request):                                                      #Функция принимающая данные с гугл таблицы каждые 5секунд
    while True:
                                                                # И отправляющая, записанные в массив данные, в html шаблон
        info_list = []
        for count, i  in enumerate(sh.sheet1.get('A1:B500')):
            if count == 0: continue
            else: 
              info_list.append([count, i[0], int(i[1])])
        counts = []
        for i in range(len(info_list)):
          counts.append(int(info_list[i][2]))
        counts = sorted(set(counts), reverse=True)
        print(counts)
        data = {'info_list':info_list, 'counts':counts}
        print(info_list[:3])
        print(counts)
        return render(request, 'main/akfa.html', context=data )
        time.sleep(10)