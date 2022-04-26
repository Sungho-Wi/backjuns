// 순열 (permutation)
fun <T> permute(input: List<T>, limit: Int = input.size, fin: List<T> = listOf()): List<List<T>> {
    return if (fin.size >= limit) {
        listOf(fin)
    } else {
        input.flatMap { permute(input - it, limit, fin + it) }
    }
}

// 중복 순열 (permutation with repetition)
fun <T> permuteWithRepetition(input: List<T>, limit: Int, fin: List<T> = listOf()): List<List<T>> {
    return if (fin.size >= limit) {
        listOf(fin)
    } else {
        input.flatMap {
            permuteWithRepetition(input, limit, fin + it)
        }
    }
}

// 조합 (combination)
fun <T> combine(input: List<T>, limit: Int, fin: List<T> = listOf()): List<List<T>> {
    return if (fin.size >= limit) {
        listOf(fin)
    } else {
        input.flatMapIndexed { index: Int, t: T ->
            combine(input.slice(index + 1 until input.size), limit, fin + t)
        }
    }
}

// 중복 조합 (combination with repetition)
fun <T> combineWithRepetition(input: List<T>, limit: Int, fin: List<T> = listOf()): List<List<T>> {
    return if (fin.size >= limit) {
        listOf(fin)
    } else {
        input.flatMapIndexed { index: Int, t: T ->
            combineWithRepetition(input.slice(index until input.size), limit, fin + t)
        }
    }
}

fun selectionSort(array: Array<Int>) {
    for (i in array.indices) {
        var minIndex = i
        for (k in i + 1 until array.size) {
            if (array[minIndex] > array[k]) {
                minIndex = k
            }
        }

        array[i] = array[minIndex].also { array[minIndex] = array[i] }
    }
}

fun insertionSort(array: Array<Int>) {
    for (i in 1 until array.size) {
        for (k in i downTo 1) {
            if (array[k] < array[k - 1]) {
                array[k] = array[k - 1].also { array[k - 1] = array[k] }
            } else {
                break
            }
        }
    }
}

fun quickSort(array: Array<Int>, start: Int = 0, end: Int = array.size - 1) {
    if (start >= end) {
        return
    }
    val pivot = start
    var left = start + 1
    var right = end
    while (left <= right) {
        while (left <= end && array[left] <= array[pivot]) {
            left += 1
        }
        while (right > start && array[right] >= array[pivot]) {
            right -= 1
        }
        if (left > right) {
            array[right] = array[pivot].also { array[pivot] = array[right] }
        } else {
            array[left] = array[right].also { array[right] = array[left] }
        }
    }

    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)
}

fun countSort(array: Array<Int>): MutableList<Int> {
    val counts = Array(100) { 0 }

    val resultList = mutableListOf<Int>()

    array.forEach {
        counts[it] += 1
    }

    for (i in counts.indices) {
        if (counts[i] == 0) {
            continue
        }

        for (k in 0 until counts[i]) {
            resultList.add(i)
        }
    }

    return resultList
}

fun binarySearch(array: List<Int>, target:Int, start: Int = 0, end: Int = array.size - 1): Int? {
    if (start > end) {
        return null
    }

    val mid = (start + end) / 2

    return if (array[mid] == target) {
        mid
    }else if (array[mid] > target) {
        binarySearch(array, target, start, mid - 1)
    } else {
        binarySearch(array, target, mid + 1, end)
    }
}

fun dijkstra(graph: Array<MutableList<Pair<Int, Int>>>, start: Int, n: Int): Array<Int> {
    val distances = Array(n + 1) { Int.MAX_VALUE }
    val heap = PriorityQueue<Pair<Int, Int>> { c1, c2 ->
        c1.first.compareTo(c2.first)
    }

    heap.add(0 to start)
    distances[start] = 0

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

fun floydWarshall() {
    val n = readLine().toInt()
    val m = readLine().toInt()

    val graph = Array(n + 1) { Array(n + 1) { INF } }

    for (a in 1..n) {
        for (b in 1..n) {
            if (a == b) {
                graph[a][b] = 0
            }
        }
    }

    for (i in 0 until m) {
        val (a, b, c) = readLine().split(" ").map { it.toInt() }
        if (graph[a][b] > c) {
            graph[a][b] = c
        }
    }

    for (k in 1..n) {
        for (a in 1..n) {
            for (b in 1..n) {
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            }
        }
    }
}

// 크루스칼 알고리즘

fun findParent(parents: Array<Int>, x: Int): Int {
    if (parents[x] != x) {
        parents[x] = findParent(parents, parents[x])
    }
    return parents[x]
}

fun unionParent(parents: Array<Int>, a: Int, b: Int) {
    val ap = findParent(parents, a)
    val bp = findParent(parents, b)

    if (ap < bp) {
        parents[bp] = parents[ap]
    } else {
        parents[ap] = parents[bp]
    }
}