import os, shutil
import backend.strings


def parseArgs():
    parser = argparse.ArgumentParser(description=_descriptionString)
    parser.add_argument('-o', '--options', type=str, help='dict containing options', default=None)
    args = parser.parse_args()

    if args.options:
        options = ast.literal_eval(args.options)
        return options
    else:
        return None


def foreplay(options: dict) -> str:
    """Foreplay before the good shit, (app initialization):
        1. Clear pycache to avoid bugs
    """
    out = "I-"

    pycache_path = os.path.join(os.getcwd(), "backend/__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)

    return "I-11"



