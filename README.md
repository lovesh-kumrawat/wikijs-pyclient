# Wikijs PyClient

A python client for an easy interaction with the WikiJS graphql API, through automating the graphql queries.

- **[Documentation](https://github.com/lovesh-kumrawat/wikijs-pyclient/wiki/Documentation)**
- **[Source Code](https://github.com/lovesh-kumrawat/wikijs-pyclient)**
- **[Bug Reports](https://github.com/lovesh-kumrawat/wikijs-pyclient/issues)**

---
## WikiJS client setup

```python
from wikijs import WikiJS
wiki = WikiJS(
    url="<protocol>://<wiki_host>:<wiki_port>",
    token="<wiki_api_key>"
)
```
