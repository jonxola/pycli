from pathlib import Path
import json
import shutil

def init():
    '''Get configuration values.
    
    If the config file exists, read it and return a Python object.
    If it doesn't, create the file with default values and return a Python object.
    If the file exists, but is invalid JSON, return None.
    '''
    defaults = Path(__file__).parent / 'defaults.json'
    file = Path.home() / '.pycli' / 'config.json'
    try:
        with file.open() as f:
            config = json.load(f)
    except FileNotFoundError:
        print('Creating default configuration file at ' + str(file) + ' ...')
        file.parent.mkdir(exist_ok=True)
        shutil.copyfile(defaults, file)
        print('Done')
        return init()
    except json.decoder.JSONDecodeError:
        print('Invalid JSON configuration at ' + str(file))
        print('Please fix the file or delete it so a new one can be generated.')
        return None
    else:
        return config