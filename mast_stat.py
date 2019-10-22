
class MastStat:
    def get_tenant_mast_count(self, list_records, key_index):
        tenant_mast_count = {}
        for item in list_records:
            if not item[key_index] in tenant_mast_count:
                tenant_mast_count[item[key_index]] = 1
            else:
                tenant_mast_count[item[key_index]] = tenant_mast_count[item[key_index]] + 1
        return tenant_mast_count
