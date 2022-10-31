import json
import os

class file_check:
    def __init__(self, file_name):
        
        if not os.path.exists(file_name):
            open(file_name, 'a').close

        if os.stat(file_name).st_size == 0:
            out_data = {
                "resource": {
                    "aws_instance": {

                    }
                }
            }
            with open(file_name, 'w') as js:
                json.dump(out_data, js, indent=4)
            js.close()

class create_vms:
    def __init__(self, vm_list, vm_config_file):
        
        with open(vm_config_file) as js:
            data = json.load(js)

        for row in vm_list.itertuples(index=True, name='Pandas'):

            data['resource']['aws_instance'][row.name] = {
                "ami": row.ami,
                "instance_type": row.instance_type,
                "key_name": row.key_name,
                "tags": {
                    "Name": row.name
            }
        }

        with open(vm_config_file, 'w') as js:
            json.dump(data, js, indent=4)

        js.close()
