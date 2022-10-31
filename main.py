import pandas
import modules

vm_config_file = "output.tf.json"
workbook = pandas.read_excel('test.xlsx')


modules.file_check(vm_config_file)
modules.create_vms(workbook, vm_config_file)