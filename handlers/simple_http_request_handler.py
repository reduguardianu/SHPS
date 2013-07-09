import http.server

class ExecuteCommand:
    command = "not_set"
    username = "not_set"
    def __init__(self, command, username):
        self.command = command
        self.username = username
    def toString(self):
        return self.username + " made action " + self.command


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if "/" == self.path:
            self.handle_login()
            return();
        command = self.get_command(self.path)
        print(command.toString())

    def handle_login(self):
        """
        """
        print("login")


    def get_command(self, path):
        command = path[1:]
        (user, permissions) = self.determine_user(self.client_address[0])
        if ("invalid" == user):
            raise "No user for this IP"
        if (not any(command == permission for permission in permissions)):
            raise "Not enough permissions!"
        return ExecuteCommand(command, user)

    def determine_user(self, address):
        users_file = open("etc/users", 'r')
        for user in users_file:
            user_info = user.split(":")
            if (user_info[0] == address):
                users_file.close()
                return (user_info[1], user_info[2].split(","))
        users_file.close()
        return ("invalid", "")
