import os


def move_file(command: str) -> None:
    try:
        command_to_run, source, destination = command.split(" ")
        if "." not in destination:
            raise ValueError
    except ValueError:
        return None

    list_destination = destination.split("/")

    if source == destination \
            or destination[-1] == "/" \
            or destination[-1] == "\\" \
            or command_to_run != "mv":
        return None

    if len(list_destination) == 1:
        os.rename(source, destination)
        return None

    path_to = ""
    for directory in list_destination[:-1]:
        path_to = os.path.join(path_to, directory)
        if not os.path.exists(path_to):
            os.mkdir(path_to)

    with open(source, "r") as source_file, \
            open(destination, "w") as destination_file:
        content = source_file.read()
        destination_file.write(content)
    os.remove(source)
