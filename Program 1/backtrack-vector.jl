import JSON

using Printf

problem = JSON.parsefile("2-moves.json")

struct Rule
    name::Symbol
    precondition::Function
    action::Function
end

"Return the (row, col) of the blank in the given state."
function blank_pos(state)
    for (i, row) in enumerate(state)
        for (j, cell) in enumerate(row)
            cell == 0 && return (i, j)
        end
    end
    error("No blank found: $state")
end

"Return a new state by moving the blank by the given delta."
function new_state(state, row_delta, col_delta)
    new_state = deepcopy(state)
    row, col = blank_pos(state)
    new_state[row][col] = new_state[row + row_delta][col + col_delta]
    new_state[row + row_delta][col + col_delta] = 0
    return new_state
end

"Sliding-Puzzle Rules"
rules = 
    [Rule(:up,
          state -> blank_pos(state)[1] != 1,
          state -> new_state(state, -1, 0)),
     Rule(:right,
          state -> blank_pos(state)[2] != length(state),
          state -> new_state(state, 0, 1)),
     Rule(:down,
          state -> blank_pos(state)[1] != length(state),
          state -> new_state(state, 1, 0)),
     Rule(:left,
          state -> blank_pos(state)[2] != 1,
          state -> new_state(state, 0, -1))
]

applicable_rules(state) = filter(rule -> rule.precondition(state), rules)

"Print a problem state."
function print_state(state)
    n = size(state, 1)
    for row in 1:n
        for col in 1:n
            if state[row][col] == 0
                print("   ")
            else
                @printf("%3i", state[row][col])
            end
        end
        println()
    end
end

count = 0

function Backtrack1(problem, datalist, bound)
    global count
    count += 1
    data = datalist[1]
    data in datalist[2:end] && return nothing
    data == problem["goal"] && return Rule[]
    length(datalist) > bound && return nothing
    for rule in applicable_rules(data)
        result = Backtrack1(problem, [rule.action(data), datalist...], bound)
        isnothing(result) || return [rule, result...]
    end
    return nothing
end

function run_once(problem, depth)
    global count = 0
    println("Start")
    print_state(problem["start"])
    solution = Backtrack1(problem, [problem["start"]], depth)
    if isnothing(solution)
        println("No solution found.")
    else
        state = problem["start"]
        for rule in solution
            println(rule.name)
            state = rule.action(state)
            print_state(state)
        end
    end
    println("$count nodes examined")
end

@time run_once(problem, 26)

function run_many(problem, limit)
    global count = 0
    println("Start")
    print_state(problem["start"])
    println("Goal")
    print_state(problem["goal"])
    for i = 0:limit
        solution = Backtrack1(problem, [problem["start"]], i)
        println("$i: $count nodes examined")
        if !isnothing(solution)
		    state = problem["start"]
            for rule in solution
                println(rule.name)
                state = rule.action(state)
                print_state(state)
            end
            break
        end
    end
end

@time run_many(problem, 30)
