def pagerank(graph, d=0.85, iterations=10):
    n = len(graph)
    
    # Step 1: initial rank
    rank = {page: 1/n for page in graph}

    # Step 2: update ranks
    for _ in range(iterations):
        new_rank = {}

        for page in graph:
            new_rank[page] = (1 - d) / n

            for p in graph:
                if page in graph[p]:  # if p links to page
                    new_rank[page] += d * (rank[p] / len(graph[p]))

        rank = new_rank

    return rank


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

print(pagerank(graph))
