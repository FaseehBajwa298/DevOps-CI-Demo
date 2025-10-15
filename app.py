import argparse


def build_message(name: str) -> str:
    return f"Hello from DevOps-CI-Demo, {name}!"


def main():
    parser = argparse.ArgumentParser(description="Simple greeting app for DevOps-CI-Demo")
    parser.add_argument("--name", default="friend", help="Name to greet")
    args = parser.parse_args()

    print(build_message(args.name))


if __name__ == "__main__":
    main()