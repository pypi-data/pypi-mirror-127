from argparse import Namespace

from dstack.config import from_yaml_file, _get_config_path


def logout_func(_: Namespace):
    config_path = _get_config_path(None)
    if config_path.exists():
        config_path.unlink()
    print("Succeeded")


def register_parsers(main_subparsers):
    parser = main_subparsers.add_parser("logout", help="Log out")

    parser.set_defaults(func=logout_func)
