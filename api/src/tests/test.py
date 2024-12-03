from utils import convert_yml_to_js, convert_js_to_yml
from prom import Blackbox

WORKDIR = "."
BL_BOX_FILE = f"{WORKDIR}/prometheus/blackbox_targets.yml"

prom_configs = {
    "blackbox_target": BL_BOX_FILE,
    "alert_rules": "",
    "prom_config": "",
    "alertmanager_config": "",
}
instance_name = "https://server10.app.funables.com"

blackbox = Blackbox(BL_BOX_FILE)

# print(blackbox.get_targets())

# print(blackbox.update_target(instance_name))

print(blackbox.remove_target(instance_name))
