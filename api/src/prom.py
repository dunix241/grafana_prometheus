from utils import convert_yml_to_js, save_to_yml
from fastapi.responses import JSONResponse


class Blackbox:
    def __init__(self, blackbox_config_path):
        self.blackbox_config_path = blackbox_config_path
        self.blackbox_target_dict = convert_yml_to_js(blackbox_config_path)
        self.target_list = self.blackbox_target_dict["targets"]

    def get_targets(self):
        return self.blackbox_target_dict

    def _update_target_dict(self, instance_name):
        if instance_name in self.target_list:
            return False
        else:
            self.target_list.append(instance_name)
            new_target_dict = {}
            new_target_dict["targets"] = self.target_list
            return [new_target_dict]

    def _remove_instance(self, instance_name):
        try:
            instance_id = self.target_list.index(instance_name)
            del self.target_list[instance_id]
            new_target_dict = {}
            new_target_dict["targets"] = self.target_list
            return [new_target_dict]
        except ValueError:
            return False

    def update_target(self, instance_name):
        new_target_dict = self._update_target_dict(instance_name)
        if new_target_dict:
            save_to_yml(
                yml_data=new_target_dict, yml_out_file=self.blackbox_config_path
            )
            return JSONResponse(
                status_code=200,
                content={
                    "message": "Update successfully",
                    "targets": new_target_dict[0]["targets"],
                },
            )
        return JSONResponse(
            status_code=202,
            content={
                "message": f"{instance_name} exists. Not modified",
                "targets": self.blackbox_target_dict["targets"],
            },
        )

    def remove_target(self, instance_name):
        new_target_dict = self._remove_instance(instance_name)
        if new_target_dict:
            save_to_yml(
                yml_data=new_target_dict, yml_out_file=self.blackbox_config_path
            )
            return JSONResponse(
                status_code=200,
                content={
                    "message": "Remove successfully",
                    "targets": new_target_dict[0]["targets"],
                },
            )
        return JSONResponse(
            status_code=202,
            content={
                "message": f"{instance_name} does not exists. Not modified",
                "targets": self.target_list,
            },
        )
