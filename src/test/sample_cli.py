import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cli_arg")
    parser.add_argument("--sleep", type=float)

    args = parser.parse_args()
    print({k: v for k, v in vars(args).items() if not k.startswith("_")})
