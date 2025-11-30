import os

from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env


def my_function(x: int, y: int) -> int:
    return x + y


def run_from_script() -> None:
    # Testando as variáveis de ambiente
    greetings = os.getenv("GREETINGS", "Not working. Read the README.md")
    print("Check dotenv:", greetings)

    # Seguindo a programação normal
    my_result = my_function(1, 2)
    print(f"The result is {my_result}")


if __name__ == "__main__":
    run_from_script()
