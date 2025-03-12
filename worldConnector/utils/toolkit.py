from pathlib import Path

def find_config_file():
    current_path = Path(__file__).resolve()
    while current_path != current_path.parent:
        config_path = current_path / "config.json"
        if config_path.exists():
            return str(config_path)
        current_path = current_path.parent
    raise FileNotFoundError("未找到 config/config.json")
