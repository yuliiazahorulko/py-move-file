import os


def move_file(command: str) -> None:
    command_to_run, source, destination = command.split(" ")
    list_destination = destination.split("/")

    if len(list_destination) == 1:
        os.rename(source, destination)
        return None

    path_to = ""
    for d in list_destination[:-1]:
        path_to += d + "/"
        if not os.path.exists(path_to):
            os.mkdir(path_to)

    with open(source, "r") as source_file, \
            open(destination, "w") as destination_file:
        content = source_file.read()
        destination_file.write(content)
    os.remove(source)
