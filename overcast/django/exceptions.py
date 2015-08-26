class CommandFailed(Exception):
    def __init__(self, msg, cmd, returncode, stdout, stderr):
        self.cmd = cmd
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        super(CommandFailed, self).__init__(msg)
