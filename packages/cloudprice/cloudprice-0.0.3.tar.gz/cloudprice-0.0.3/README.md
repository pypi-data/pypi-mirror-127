# cloud-compute-pricing
[![image](https://img.shields.io/pypi/v/cloudprice.svg)](https://pypi.org/project/cloudprice/)
[![image](https://pepy.tech/badge/cloudprice)](https://pepy.tech/project/geodemo)
[![image](https://github.com/guanjieshen/cloud-compute-pricing/workflows/build/badge.svg)](https://github.com/giswqs/geodemo/actions?query=workflow%3Abuild)
[![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Examples
For more examples see the `examples` directory with this repo.

#### Azure Virtual Machines
Currently for Azure VMs there is support for `On Demand`, `Spot`, `Low Priority`, and `Reserved Instance` pricing. 

Using the default parameters will return the price for the __Linux On Demand VM__.

See example below on how to use the `AzureVM` module. 

```python
from cloudprice import AzureVM

# Get Azure VM Pricing
example_vm = AzureVM("US West", "Standard_E8_v3")

# Get Azure VM Pricing for On Demand Instance
example_vm_standard = example_vm.getPrice()
print(
    f"""
Product Name: {example_vm_standard.product_name}
Meter Name: {example_vm_standard.meter_name}
Location: {example_vm_standard.location}
Effective Date: {example_vm_standard.effective_start_date}
Unit Price: {example_vm_standard.unit_price}
"""
)

```