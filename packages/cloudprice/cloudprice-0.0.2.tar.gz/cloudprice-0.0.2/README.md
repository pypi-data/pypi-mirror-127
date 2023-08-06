# cloud-compute-pricing

### Examples



```python
from cloudprice.azure import AzureVM

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