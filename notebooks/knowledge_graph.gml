graph [
  directed 1
  node [
    id 0
    label "2408.08921"
    type "paper"
    title "Graph Retrieval-Augmented Generation: A Survey"
    year "2024"
    abstract "Recently, Retrieval-Augmented Generation (RAG) has achieved remarkable success in addressing the challenges of Large Language Models (LLMs) without necessitating retraining. By referencing an external knowledge base, RAG refines LLM outputs, effectively mitigating issues such as ``hallucination'', lack of domain-specific knowledge, and outdated information. However, the complex structure of relationships among different entities in databases presents challenges for RAG systems. In response, GraphRAG leverages structural information across entities to enable more precise and comprehensive retrieval, capturing relational knowledge and facilitating more accurate, context-aware responses. Given the novelty and potential of GraphRAG, a systematic review of current technologies is imperative. This paper provides the first comprehensive overview of GraphRAG methodologies. We formalize the GraphRAG workflow, encompassing Graph-Based Indexing, Graph-Guided Retrieval, and Graph-Enhanced Generation. We then outline the core technologies and training methods at each stage. Additionally, we examine downstream tasks, application domains, evaluation methodologies, and industrial use cases of GraphRAG. Finally, we explore future research directions to inspire further inquiries and advance progress in the field. In order to track recent progress in this field, we set up a repository at \url{this https URL}."
  ]
  node [
    id 1
    label "Boci Peng"
    type "author"
  ]
  node [
    id 2
    label "Yun Zhu"
    type "author"
  ]
  node [
    id 3
    label "Yongchao Liu"
    type "author"
  ]
  node [
    id 4
    label "Xiaohe Bo"
    type "author"
  ]
  node [
    id 5
    label "Haizhou Shi"
    type "author"
  ]
  node [
    id 6
    label "Chuntao Hong"
    type "author"
  ]
  node [
    id 7
    label "Yan Zhang"
    type "author"
  ]
  node [
    id 8
    label "Siliang Tang"
    type "author"
  ]
  node [
    id 9
    label "2405.16506"
    type "paper"
    title "GRAG: Graph Retrieval-Augmented Generation"
    year "2024"
    abstract "Naive Retrieval-Augmented Generation (RAG) focuses on individual documents during retrieval and, as a result, falls short in handling networked documents which are very popular in many applications such as citation graphs, social media, and knowledge graphs. To overcome this limitation, we introduce Graph Retrieval-Augmented Generation (GRAG), which tackles the fundamental challenges in retrieving textual subgraphs and integrating the joint textual and topological information into Large Language Models (LLMs) to enhance its generation. To enable efficient textual subgraph retrieval, we propose a novel divide-and-conquer strategy that retrieves the optimal subgraph structure in linear time. To achieve graph context-aware generation, incorporate textual graphs into LLMs through two complementary views-the text view and the graph view-enabling LLMs to more effectively comprehend and utilize the graph context. Extensive experiments on graph reasoning benchmarks demonstrate that in scenarios requiring multi-hop reasoning on textual graphs, our GRAG approach significantly outperforms current state-of-the-art RAG methods."
  ]
  node [
    id 10
    label "Yuntong Hu"
    type "author"
  ]
  node [
    id 11
    label "Zhihan Lei"
    type "author"
  ]
  node [
    id 12
    label "Zheng Zhang"
    type "author"
  ]
  node [
    id 13
    label "Bo Pan"
    type "author"
  ]
  node [
    id 14
    label "Chen Ling"
    type "author"
  ]
  node [
    id 15
    label "Liang Zhao"
    type "author"
  ]
  edge [
    source 0
    target 1
    relation "authored_by"
  ]
  edge [
    source 0
    target 2
    relation "authored_by"
  ]
  edge [
    source 0
    target 3
    relation "authored_by"
  ]
  edge [
    source 0
    target 4
    relation "authored_by"
  ]
  edge [
    source 0
    target 5
    relation "authored_by"
  ]
  edge [
    source 0
    target 6
    relation "authored_by"
  ]
  edge [
    source 0
    target 7
    relation "authored_by"
  ]
  edge [
    source 0
    target 8
    relation "authored_by"
  ]
  edge [
    source 0
    target 9
    relation "cites"
  ]
  edge [
    source 1
    target 0
    relation "is_author"
  ]
  edge [
    source 2
    target 0
    relation "is_author"
  ]
  edge [
    source 3
    target 0
    relation "is_author"
  ]
  edge [
    source 4
    target 0
    relation "is_author"
  ]
  edge [
    source 5
    target 0
    relation "is_author"
  ]
  edge [
    source 6
    target 0
    relation "is_author"
  ]
  edge [
    source 7
    target 0
    relation "is_author"
  ]
  edge [
    source 8
    target 0
    relation "is_author"
  ]
  edge [
    source 9
    target 10
    relation "authored_by"
  ]
  edge [
    source 9
    target 11
    relation "authored_by"
  ]
  edge [
    source 9
    target 12
    relation "authored_by"
  ]
  edge [
    source 9
    target 13
    relation "authored_by"
  ]
  edge [
    source 9
    target 14
    relation "authored_by"
  ]
  edge [
    source 9
    target 15
    relation "authored_by"
  ]
  edge [
    source 9
    target 0
    relation "cited_in"
  ]
  edge [
    source 10
    target 9
    relation "is_author"
  ]
  edge [
    source 11
    target 9
    relation "is_author"
  ]
  edge [
    source 12
    target 9
    relation "is_author"
  ]
  edge [
    source 13
    target 9
    relation "is_author"
  ]
  edge [
    source 14
    target 9
    relation "is_author"
  ]
  edge [
    source 15
    target 9
    relation "is_author"
  ]
]
