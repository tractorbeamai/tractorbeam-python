# Documents

Types:

```python
from tractorbeam.types import Document, DocumentListResponse
```

Methods:

- <code title="post /documents">client.documents.<a href="./src/tractorbeam/resources/documents.py">create</a>(\*\*<a href="src/tractorbeam/types/document_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/document.py">Document</a></code>
- <code title="get /documents">client.documents.<a href="./src/tractorbeam/resources/documents.py">list</a>() -> <a href="./src/tractorbeam/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/{id}">client.documents.<a href="./src/tractorbeam/resources/documents.py">delete</a>(id) -> None</code>
- <code title="get /documents/{id}/contents">client.documents.<a href="./src/tractorbeam/resources/documents.py">contents</a>(id) -> None</code>
- <code title="get /documents/{id}">client.documents.<a href="./src/tractorbeam/resources/documents.py">get</a>(id) -> <a href="./src/tractorbeam/types/document.py">Document</a></code>
- <code title="get /documents/{id}/tuples">client.documents.<a href="./src/tractorbeam/resources/documents.py">tuples</a>(id, \*\*<a href="src/tractorbeam/types/document_tuples_params.py">params</a>) -> None</code>

# Graphs

Types:

```python
from tractorbeam.types import (
    Graph,
    GraphListResponse,
    GraphAddTuplesResponse,
    GraphGetTuplesResponse,
)
```

Methods:

- <code title="post /graphs">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">create</a>(\*\*<a href="src/tractorbeam/types/graph_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/graph.py">Graph</a></code>
- <code title="get /graphs">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">list</a>() -> <a href="./src/tractorbeam/types/graph_list_response.py">GraphListResponse</a></code>
- <code title="delete /graphs/{owner}/{name}">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">delete</a>(name, \*, owner) -> None</code>
- <code title="post /graphs/{owner}/{name}/tuples">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">add_tuples</a>(name, \*, owner, \*\*<a href="src/tractorbeam/types/graph_add_tuples_params.py">params</a>) -> <a href="./src/tractorbeam/types/graph_add_tuples_response.py">GraphAddTuplesResponse</a></code>
- <code title="get /graphs/{owner}/{name}">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">get</a>(name, \*, owner) -> <a href="./src/tractorbeam/types/graph.py">Graph</a></code>
- <code title="get /graphs/{owner}/{name}/tuples">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">get_tuples</a>(name, \*, owner) -> <a href="./src/tractorbeam/types/graph_get_tuples_response.py">GraphGetTuplesResponse</a></code>

# Health

Types:

```python
from tractorbeam.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/tractorbeam/resources/health.py">check</a>() -> <a href="./src/tractorbeam/types/health_check_response.py">HealthCheckResponse</a></code>
