from rich.console import Console
from rich.prompt import Prompt

console = Console()

def length_list(lst: list) -> int:
    return len(lst)

def is_even(elements: list) -> bool:
    return length_list(elements) % 2 == 0
    

def main():
    names = []

    while True:
        name = input("Ism kiriting: ").title()
        names.append(name)

        option = Prompt.ask(
            "Yana ism kiritasizmi?: ",
            choices=["ha", "yo'q"], 
            default="yo'q",
            case_sensitive=False
        )
        
        if option == "yo'q":
            break

    result = is_even(names)

    console.print(f"Ismlar soni juftmi? → [bold magenta]{result}[/bold magenta]")

main()
