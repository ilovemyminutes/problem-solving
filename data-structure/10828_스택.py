n = int(input())
stack = []
output = ''

for _ in range(n):
    command = input().split()

    # push: no print
    if len(command) > 1:
        value = int(command[1])
        stack.append(value)

    else:
        command = command[0]
        if command == 'top':
            if len(stack) > 0:
                output += f"{stack[-1]}\n"
            else:
                output += f"-1\n"
                
        elif command == 'pop':
            if len(stack) > 0:
                popped = stack.pop()
                output += f"{popped}\n"
            else:
                output += f"-1\n"

        elif command == 'size':
            output += f"{len(stack)}\n"

        elif command == 'empty':
            if len(stack) == 0:
                output += f"1\n"
            else:
                output += f"0\n"
print(output)
    