class Solution:
    def interpret(self, command: str) -> str:
        commands = command.replace("()", "o")

        commands = commands.replace("(", "")
        commands = commands.replace(")", "")
        return commands


if __name__ == "__main__":
    obj = Solution()
    command = "G()(al)"
    print(obj.interpret(command))