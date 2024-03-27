# PDF 文件的 URL
from pathlib import Path
import requests
filename = Path('/Users/mac/Desktop/metadata111122.pdf')
url = 'http://192.168.84.29:9000/nlp/nlpmp/am-doc/1111/1772181943879323650/BPO%E6%8B%9B%E8%81%98%E7%94%B5%E5%AD%90%E5%8C%96%E6%93%8D%E4%BD%9C%E6%89%8B%E5%86%8C%20-%20%E5%80%99%E9%80%89%E4%BA%BAV1.5.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=nlpadmin%2F20240325%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240325T084117Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=5f887235d3c90b8166b130ad05b4f32e79b150a3cb9d9df2f5756793b05c204c'
response = requests.get(url)
filename.write_bytes(response.content)

