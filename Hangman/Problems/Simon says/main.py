def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return f"I {instructions[len('Simon says')+1:]}"
    elif instructions.endswith("Simon says"):
        return f"I {instructions[:instructions.index('Simon says')]}"
    return "I won't do it!"
