# Shared Types

```python
from tractorbeam.types import DocumentContents
```

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
from tractorbeam.types import Document, DocumentListResponse
```

Methods:

- <code title="post /documents">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">create</a>(\*\*<a href="src/tractorbeam/types/document_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/document.py">Document</a></code>
- <code title="get /documents/{id}">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">retrieve</a>(id) -> <a href="./src/tractorbeam/types/document.py">Document</a></code>
- <code title="get /documents">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">list</a>() -> <a href="./src/tractorbeam/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/{id}">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">delete</a>(id) -> None</code>
- <code title="get /documents/{id}/tuples">client.documents.<a href="./src/tractorbeam/resources/documents/documents.py">tuples</a>(id, \*\*<a href="src/tractorbeam/types/document_tuples_params.py">params</a>) -> None</code>

## Contents

Methods:

- <code title="get /documents/{id}/contents">client.documents.contents.<a href="./src/tractorbeam/resources/documents/contents.py">retrieve</a>(id) -> <a href="./src/tractorbeam/types/shared/document_contents.py">DocumentContents</a></code>

# Graphs

Types:

```python
from tractorbeam.types import Graph, GraphListResponse, GraphQueryResponse
```

Methods:

- <code title="post /graphs">client.graphs.<a href="./src/tractorbeam/resources/graphs/graphs.py">create</a>(\*\*<a href="src/tractorbeam/types/graph_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/graph.py">Graph</a></code>
- <code title="get /graphs/{owner}/{name}">client.graphs.<a href="./src/tractorbeam/resources/graphs/graphs.py">retrieve</a>(name, \*, owner) -> <a href="./src/tractorbeam/types/graph.py">Graph</a></code>
- <code title="get /graphs">client.graphs.<a href="./src/tractorbeam/resources/graphs/graphs.py">list</a>() -> <a href="./src/tractorbeam/types/graph_list_response.py">GraphListResponse</a></code>
- <code title="delete /graphs/{owner}/{name}">client.graphs.<a href="./src/tractorbeam/resources/graphs/graphs.py">delete</a>(name, \*, owner) -> None</code>
- <code title="post /graphs/{owner}/{name}/query">client.graphs.<a href="./src/tractorbeam/resources/graphs/graphs.py">query</a>(name, \*, owner, \*\*<a href="src/tractorbeam/types/graph_query_params.py">params</a>) -> <a href="./src/tractorbeam/types/graph_query_response.py">GraphQueryResponse</a></code>

## Tuples

Types:

```python
from tractorbeam.types.graphs import TupleCreateResponse
```

Methods:

- <code title="post /graphs/{owner}/{name}/tuples">client.graphs.tuples.<a href="./src/tractorbeam/resources/graphs/tuples.py">create</a>(name, \*, owner, \*\*<a href="src/tractorbeam/types/graphs/tuple_create_params.py">params</a>) -> <a href="./src/tractorbeam/types/graphs/tuple_create_response.py">TupleCreateResponse</a></code>

# Health

Types:

```python
from tractorbeam.types import HealthRestrictResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/tractorbeam/resources/health.py">restrict</a>() -> <a href="./src/tractorbeam/types/health_restrict_response.py">HealthRestrictResponse</a></code>

# Queries

Types:

```python
from tractorbeam.types import QueryDecodeResponse
```

Methods:

- <code title="post /queries/decode">client.queries.<a href="./src/tractorbeam/resources/queries.py">decode</a>(\*\*<a href="src/tractorbeam/types/query_decode_params.py">params</a>) -> <a href="./src/tractorbeam/types/query_decode_response.py">QueryDecodeResponse</a></code>

# Query

Types:

```python
from tractorbeam.types import QueryRestrictResponse
```

Methods:

- <code title="post /query">client.query.<a href="./src/tractorbeam/resources/query.py">restrict</a>(\*\*<a href="src/tractorbeam/types/query_restrict_params.py">params</a>) -> <a href="./src/tractorbeam/types/query_restrict_response.py">QueryRestrictResponse</a></code>
