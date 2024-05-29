# -*- coding: utf-8 -*-
import base64


content = 'jVzHKeb6wZY5rzSZRx866aUQ5moxW7MJGZITGNNW4hR99MSAMZ4Mn+re6+TJ9horP4xIQdK9EoHsWlPvwc5dZK7uMN+TbZL4I+PHNRC5nnK1XslmLMXzSB0yvURqq5gQOBym83BZ+6HhGg68zJEOCixiK3N7XMgbLpwgVGWRxbK7rkaybuXyeKhoy8+PAw0xu3Q53cZg4oFcOWSGEvhc6IEfSHIatk1D59ik/Iom5kYROp3ClERJBzK7bEw7WRUYab7NldwqoC0XbCD5Hs91iVNDCZNg6YmSJv5MFfsnXy5i3ZZPsbeahejuhpkdcxaHE4SHkHnfHlwqfEvrpJpb5A=='
result = base64.b64decode(content).decode('utf8', errors='ignore')
print(result)