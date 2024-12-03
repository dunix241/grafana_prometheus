import json
import yaml
from ruamel.yaml import YAML


def save_to_js(json_output_file, json_data={}):
    # Write JSON data to a file
    with open(json_output_file, "w") as json_file:
        json_file.write(json_data)


def convert_yml_to_js(yml_file):
    with open(yml_file, "r") as yaml_file:
        yaml = YAML(typ="safe", pure=True)
        res = yaml.load(yaml_file)

    return res[0]


def convert_js_to_yml(js_data):
    return yaml.dump(js_data)


def save_to_yml(yml_data="", yml_out_file="./sample.yml"):
    with open(yml_out_file, "w") as yml_file:
        yaml.dump(yml_data, yml_file, default_flow_style=False)
