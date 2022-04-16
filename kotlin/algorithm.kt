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