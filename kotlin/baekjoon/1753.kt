import java.util.*

fun main() {
    with(System.`in`.bufferedReader()) {
        val (n, e) = readLine().split(" ").map { it.toInt() }
        val start = readLine().toInt()

        val graph = Array(n + 1) { mutableListOf<Pair<Int, Int>>() }

        for (i in 0 until e) {
            val (u, v, w) = readLine().split(" ").map { it.toInt() }
            graph[u].add(v to w)
        }

        val distances = dijkstra(graph, start, n)

        for (i in 1 until n + 1) {
            val distance = if (distances[i] != Int.MAX_VALUE) {
                distances[i].toString()
            } else {
                "INF"
            }

            println(distance)
        }
    }
}

fun dijkstra(graph: Array<MutableList<Pair<Int, Int>>>, start: Int, n: Int): Array<Int> {
    val distances = Array(n + 1) { Int.MAX_VALUE }

    val heap = PriorityQueue<Pair<Int, Int>> { c1, c2 ->
        c1.first.compareTo(c2.first)
    }

    distances[start] = 0
    heap.add(0 to start)

    while (heap.isNotEmpty()) {
        val (dist, now) = heap.poll()

        if (distances[now] < dist) {
            continue
        }

        for ((v, w) in graph[now]) {
            val cost = dist + w

            if (cost < distances[v]) {
                distances[v] = cost
                heap.add(cost to v)
            }
        }

    }

    return distances
}