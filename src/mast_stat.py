import re

# Create Mast Statistics from given raw data.
class MastStat:
    # Calculates masts count grouped by tenants name.
    def get_tenant_mast_count(self, list_records, key_index):
        tenant_mast_count = {}
        for item in list_records:
            key_name = item[key_index]
            if not item[key_index] in tenant_mast_count:
                tenant_mast_count[key_name] = 1
            else:
                tenant_mast_count[key_name] = tenant_mast_count[key_name] + 1
        return tenant_mast_count

    # Aggregates given columns from raw data.
    def aggregate(self, list_records, key_index):
        total = 0
        for item in list_records:
            total += float(item[key_index])
        return total

