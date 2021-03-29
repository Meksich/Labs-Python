def main():
    START_TIME = b"[01/Jul/1995:00:10:"
    END_TIME = b"[01/Jul/1995:00:20:"
    KEY_PHRASE = b"NASA"
    is_needed_time = False
    line_counter = 0

    with open("access_log_Jul95", 'rb') as a:
        file = a.readlines()

    for line in file:
        if END_TIME in line:
            is_needed_time = False
            break
        if START_TIME in line:
            is_needed_time = True
        if is_needed_time and KEY_PHRASE in line:
            line_counter = line_counter + 1

    print(line_counter)


if __name__ == '__main__':
    main()
