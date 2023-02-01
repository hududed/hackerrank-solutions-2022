def connected(graph_nodes, graph_from, graph_to):
    unseen = [i for i in range(1, graph_nodes + 1)]
    edges = [[graph_from[i], graph_to[i]] for i in range(len(graph_from))]

    connects = []

    while unseen != []:
        start = unseen[0]
        connection = []

        queue = [start]
        unseen.remove(start)

        while queue != []:

            end = queue[-1]

            if end not in connection:
                connection.append(end)

            queue = queue[:-1]

            print(unseen, edges)
            for k in edges:
                if k[0] == end:
                    queue.append(k[1])
                    unseen.remove(k[1])

        connects.append(connection)

    return connects


def main():
    # graph_nodes, graph_from, graph_to = 10, [1, 1, 2, 3, 7], [2, 3, 4, 5, 8]
    graph_nodes = 8
    graph_to = [1, 1, 3, 5, 6]
    graph_from = [2, 6, 4, 7, 3]

    # graph_nodes, graph_from, graph_to = 10, [1, 1, 2, 3, 7], [2, 3, 4, 5, 8]
    print(connected(graph_nodes, graph_from, graph_to))


if __name__ == "__main__":
    main()
