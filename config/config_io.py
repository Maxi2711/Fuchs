from config.config_class import Config
import json

class Config_IO:
    def load_config(path: str) -> Config:
        output = Config()
        f = open(path,"r")
        data = json.loads(f.read())
        f.close()
        output.import_dictionary(data)

        return output

    def save_config(cfg: Config, path: str) -> None: 
        f = open(path,"w")
        f.write(json.dumps(cfg.dictionary(), indent=4))
        f.close()