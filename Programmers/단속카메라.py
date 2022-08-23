import copy


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1], reverse=False)
    while routes:
        camera = routes[0][1]
        for route in routes[:]:
            if route[0] <= camera:
                routes.remove(route)
        answer += 1
    return answer


if __name__ == "__main__":
    routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
    print(solution(routes))
