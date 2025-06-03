import os, sys, shutil, json, psutil, time, threading
from backend.exceptions import *

def loadOptions():
    """Load in launch options"""
    optPath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "marionette")), 'options.json')
    if os.path.isfile(optPath):
        try:
            with open(optPath, 'r') as f:
                options = json.load(f)
                return options
        except json.JSONDecodeError:
            raise InvalidJSONFormat("options.json is not a valid json file.")
    else:
        return None


def cpuLimiter(cores: int) -> str:
    """Set number of cores"""
    try:
        out = "CL-"
        totalCores = os.cpu_count()
        if totalCores is None:
            cores = 1
            log("UNABLE TO DETERMINE TOTAL CORES, USING 1 CORE", 2)
        elif cores is None or cores > totalCores or cores < 1:
            raise LimitError("Invalid or missing 'cpu_cores' value.")
        else:
            out += "1"
        
        pid = psutil.Process(os.getpid())
        pid.cpu_affinity(list(range(cores)))
        out += "1"
        return out
    except LimitError as e:
        log(f"Error in setting max cpu cores: {e}", 3)
        sys.exit(1)


def memoryLimiter(allotedMemory: int):
    """Monitor memory usage and kill process as needed"""
    try:
        out = "ML-"
        if allotedMemory is None or allotedMemory < 1:
            raise LimitError("Invalid or missing 'mem_alloc' value.")
        else:
            out += "1"

        pid = psutil.Process(os.getpid())

        def memoryWatcher():
            while True:
                usage = pid.memory_info().rss / 1048576
                if usage > allotedMemory:
                    log(f"Memory limit exceeded! ({usage:.2f} MiB > {allotedMemory} MiB). Killing process.", 1)
                    pid.terminate()
                    break
                time.sleep(1)

        thread = threading.Thread(target=memoryWatcher, daemon=True)
        thread.start()
        return out
    except LimitError as e:
        log(f"Error in setting max memory limit: {e}", 3)
        sys.exit(1)


def foreplay(options: dict) -> str:
    """Foreplay before the good shit, (app initialization):
        1. Clear pycache to avoid bugs
        2. Allocate cpu cores and memory to app
    """
    out = "I-"

    if options is None:
        log("Launch options do not exist", 3)
        out += "0"
        return out
    else:
        k = cpuLimiter(options.get("cpu-cores"))
        log(f"Successfully set max cores to {options.get('cpu-cores')}; code: [{k}]")
        out += "1"
        k = memoryLimiter(options.get("mem-alloc"))
        log(f"Successfuly allocated {options.get('mem-alloc')}MiB of memory; code: [{k}]")
        out += "1"

    pycache_path = os.path.join(os.getcwd(), "backend/__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)

    return out



def log(msg: str, code: int = 0) -> None:
    """Print stuff with proper formatting
       0 -> OK
       1 -> INFO
       2 -> WARN
       3 -> FAIL    
    """
    labels = {0: (" OK ", 32), 1: ("INFO", 34), 2: ("WARN", 33), 3: ("FAIL", 31)}
    tag, color = labels.get(code, ("???? ", 37))
    print(f"\033[37m[\033[0m \033[{color}m{tag}\033[0m \033[37m] {msg}\033[0m")