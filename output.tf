resource "vcd_vapp_vm" "vm1" {
  name    = "vm1"
  os      = "linux"
  memory  = 16
  cpus    = 4
}