import os
import requests

print(os.getcwd())
dirname  = os.path.dirname(__file__)
dfile = open(dirname+"/../../target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar.original", "rb")
auth = ("admin", "Admin@123")
url = "http://13.57.36.104:8082/artifactory/example-repo-local/"
test_res = requests.put(url, files = {"doc_ja": dfile},auth=auth)
if test_res.ok:
    print(" File uploaded successfully ! ")
    print(test_res.text)
    print(test_res.status_code)
else:
    print("File upload is failed")
    print(test_res.status_code)