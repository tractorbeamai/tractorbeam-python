# Tractorbeam

Types:

```python
from tractorbeam.types import HealthCheckResponse, QueryResponse
```

Methods:

- <code title="get /health">client.<a href="./src/tractorbeam/_client.py">health_check</a>() -> <a href="./src/tractorbeam/types/health_check_response.py">HealthCheckResponse</a></code>
- <code title="post /query">client.<a href="./src/tractorbeam/_client.py">query</a>(\*\*<a href="src/tractorbeam/types/client_query_params.py">params</a>) -> <a href="./src/tractorbeam/types/query_response.py">QueryResponse</a></code>

# APITokens

Types:

```python
from tractorbeam.types import APIToken, APITokenListResponse
```

Methods:

- <code title="post /api-tokens">client.api_tokens.<a href="./src/tractorbeam/resources/api_tokens.py">create</a>(\*\*<a href="src/tractorbeam/types/api_token_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/api_token.py">APIToken</a></code>
- <code title="get /api-tokens/{id}">client.api_tokens.<a href="./src/tractorbeam/resources/api_tokens.py">retrieve</a>(id) -> <a href="./src/tractorbeam/types/api_token.py">APIToken</a></code>
- <code title="get /api-tokens">client.api_tokens.<a href="./src/tractorbeam/resources/api_tokens.py">list</a>() -> <a href="./src/tractorbeam/types/api_token_list_response.py">APITokenListResponse</a></code>
- <code title="delete /api-tokens/{id}">client.api_tokens.<a href="./src/tractorbeam/resources/api_tokens.py">delete</a>(id) -> None</code>

# Documents

Types:

```python
from tractorbeam.types import Document, DocumentContents, DocumentListResponse
```

Methods:

- <code title="post /documents">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">create</a>(\*\*<a href="src/tractorbeam/types/document_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/document.py">Document</a></code>
- <code title="get /documents/{id}">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">retrieve</a>(id) -> <a href="./src/tractorbeam/types/document.py">Document</a></code>
- <code title="get /documents">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">list</a>() -> <a href="./src/tractorbeam/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/{id}">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">delete</a>(id) -> None</code>

## Contents

Methods:

- <code title="get /documents/{id}/contents">client.documents.contents.<a href="./src/tractorbeam/resources/documents/contents.py">retrieve</a>(id) -> <a href="./src/tractorbeam/types/document_contents.py">DocumentContents</a></code>

## Tuples

Methods:

- <code title="get /documents/{id}/tuples">client.documents.tuples.<a href="./src/tractorbeam/resources/documents/tuples.py">list</a>(id, \*\*<a href="src/tractorbeam/types/documents/tuple_list_params.py">params</a>) -> None</code>

# Graphs

Types:

```python
from tractorbeam.types import Graph, GraphListResponse, GraphQueryResponse, GraphTuplesResponse
```

Methods:

- <code title="post /graphs">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">create</a>(\*\*<a href="src/tractorbeam/types/graph_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/graph.py">Graph</a></code>
- <code title="get /graphs/{owner}/{name}">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">retrieve</a>(name, \*, owner) -> <a href="./src/tractorbeam/types/graph.py">Graph</a></code>
- <code title="get /graphs">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">list</a>() -> <a href="./src/tractorbeam/types/graph_list_response.py">GraphListResponse</a></code>
- <code title="delete /graphs/{owner}/{name}">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">delete</a>(name, \*, owner) -> None</code>
- <code title="post /graphs/{owner}/{name}/query">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">query</a>(name, \*, owner, \*\*<a href="src/tractorbeam/types/graph_query_params.py">params</a>) -> <a href="./src/tractorbeam/types/graph_query_response.py">GraphQueryResponse</a></code>
- <code title="post /graphs/{owner}/{name}/tuples">client.graphs.<a href="./src/tractorbeam/resources/graphs.py">tuples</a>(name, \*, owner, \*\*<a href="src/tractorbeam/types/graph_tuples_params.py">params</a>) -> <a href="./src/tractorbeam/types/graph_tuples_response.py">GraphTuplesResponse</a></code>

# Queries

Types:

```python
from tractorbeam.types import QueryDecodeResponse
```

Methods:

- <code title="post /queries/decode">client.queries.<a href="./src/tractorbeam/resources/queries.py">decode</a>(\*\*<a href="src/tractorbeam/types/query_decode_params.py">params</a>) -> <a href="./src/tractorbeam/types/query_decode_response.py">QueryDecodeResponse</a></code>
