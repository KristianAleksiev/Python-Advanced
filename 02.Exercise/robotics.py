from collections import deque


def read_robots():
    """All robots on the processing line"""
    result = {}
    robots_input = input().split(";")

    for robot_input in robots_input:
        robot_details = robot_input.split("-")
        name = robot_details[0]
        processing_time = int(robot_details[1])
        result[name] = processing_time

    return result


def to_seconds(hours, minutes, seconds):
    """Converting the input hour format H:M:S to seconds"""
    return hours * 3600 + minutes * 60 + seconds


def read_products():
    """Checking the input for a valid product or an end of processing"""
    result = deque()

    while True:
        line = input()

        if line == "End":
            break

        result.append(line)
    return result


def to_string_time(total_seconds):
    """Reformatting the time output from seconds to H:M:S"""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = (total_seconds % 3600) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = read_robots()
available_robots = [k for k in robots.keys()]
processing_robots = {}  # Which are unavailable

starting_time_parts = [int(x) for x in input().split(":")]

time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])

products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 3600)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1

        if processing_robots[robot_name] <= 0:  # Robot processing instantly
            processing_robots.pop(robot_name)

    current_product = products.popleft()

    for robot_name in available_robots:

        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} [{to_string_time(time_in_seconds)}]")
            processing_robots[robot_name] = robots[robot_name]  # Processing time for the current robot
            break

    else:  # No robot available for current product, re-adding for next try
        products.append(current_product)
