def parse_input(user_input: str) -> (str, list):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
