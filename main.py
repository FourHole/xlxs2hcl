import pandas as xl
import modules

output = open("output.txt","w")

workbook = xl.read_excel('test.xlsx')

for row in workbook.itertuples(index=True, name='Pandas'):
    vm = modules.create_vapp_vm(row.name, row.os, row.ram, row.cpu)
    print(str(vm))

#print(workbook.loc[1]['name'])