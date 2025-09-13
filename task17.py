from rich.console import Console
from rich.prompt import Prompt

console = Console()

def print_length(list: list):
    console.print("Ismlar soni: ", len(list), style="green")
    

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
        
        if option == "ha":
            continue
        elif option == "yo'q":
            break

    print_length(names)

    


main()