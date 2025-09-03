tables = [
    'MSTDTL_M','CDSITM_M','BCLCTC_M','CPNPMO_M','PROOLN_M','PROORD_M',
    'CDSCTM_M','MSTORD_M','CDSADR_M','CDSEML_M','ARPPAP_M','ARPPCH_M','ARPPDH_M',
    'cirsub_m','AMBPAR_M','AMBTRM_M','AMBAPT_M','AMBAGR_M','CDSCTM_M_','AMBSTS_N',
    'CIRPUB_T','CPNOFR_M','CIRDTL_M','CIRHDR_M','BCLCDT_M','bclevt_m','AMBAGO_M',
    'AMBOLN_M','ATMOLN_M'
]

query_list = []

for table in tables:
    query_list.append(f"SELECT '{table}' AS table_name, COUNT(*) AS row_count FROM cds_core_lakehouse.{table} WHERE cds_client_p = 'BPACC'")

# Join all queries using UNION ALL
final_query = "\nUNION ALL\n".join(query_list)

print(final_query)