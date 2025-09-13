from rich.console import Console
from rich.prompt import Prompt

console = Console()
elements = []
counter = 0

while True:
    element = Prompt.ask("Element qo'shing")
    elements.append(element)
    counter += 1

    option = Prompt.ask(
        "Yana element qo'shasizmi?", 
        choices=["ha", "yo'q"],
        case_sensitive=False,
        default="yo'q"
    )

    if option == "ha":
        continue
    elif option == "yo'q":
        break

if counter > 5:
    console.print("Ko'p element", style="red")
else:
    console.print("Good Job!", style="green")
