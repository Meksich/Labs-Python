import re


def main():
    is_needed_time = False
    line_counter = 0
    file = open("access_log_Jul95")

    for line in file:
        if re.search(r"01/Jul/1995:00:20:\d\d", line) is not None:
            is_needed_time = False
            break
        if re.search(r"01/Jul/1995:00:10:\d\d", line) is not None:
            is_needed_time = True
        if is_needed_time and re.search(r"NASA", line) is not None:
            line_counter = line_counter + 1

    print(line_counter)


if __name__ == '__main__':
    main()
