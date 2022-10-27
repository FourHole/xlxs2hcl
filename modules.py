class create_vapp_vm:
    def __init__(self, name, os, ram, cpu):
        self.name = name
        self.os = os
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        return (
            f'resource "vcd_vapp_vm" "{self.name}" {{\n' 
            f'  name    = "{self.name}"\n' 
            f'  os      = "{self.os}"\n' 
            f'  memory  = {self.ram}\n' 
            f'  cpus    = {self.cpu}\n' 
            f'}}'
        )
        
#vm1 = vm('vm1','linux',16,4)

#f = open("output.tf", "w")

#f.write(str(vm1))
#f.close()