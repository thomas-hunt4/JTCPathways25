# Examples of importing in Python

from myfunctions import module
# import module 

def main () -> None:
    # Entrypoint of program
    print(module.powerful(2, 4))
    print(f"The answer: {module.THE_ANSWER}")


if __name__ == "__main__":
    main()

