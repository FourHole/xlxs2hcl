import pandas as xl
import json
import modules

vm_config_file = "output.tf.json"

workbook = xl.read_excel('test.xlsx')

with open(vm_config_file) as js:
    data = json.load(js)

for row in workbook.itertuples(index=True, name='Pandas'):
    
    data['resource']['aws_instance'][row.name] = {
        "name": row.name,
        "os": row.os,
        "ram": row.ram,
        "cpu": row.cpu
    }

with open(vm_config_file, 'w') as js:
    json.dump(data, js, indent=4)

js.close()