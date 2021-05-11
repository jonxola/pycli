from . import config
from . import cli

def run():
    cfg = config.init()
    args = cli.init()