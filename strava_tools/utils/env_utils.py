import dotenv

def env_get(key):
    """
    Returns the value of an environment variable.
    """
    return dotenv.dotenv_values().get(key)

def env_set(key, value):
    """
    Sets environment variables by rewriting the .env file.
    """
    config = dotenv.dotenv_values()
    config[key] = value

    with open('.env', 'w') as f:
        for key, value in config.items():
            if type(value) is int:
                f.write(f'{key}={value}\n')
            elif value.isnumeric():
                f.write(f'{key}={value}\n')
            else:
                f.write(f'{key}="{value}"\n')
