import requests
import json
from azure.common.credentials import ServicePrincipalCredentials
from azure import loganalytics

TENANT_ID = '' # 目錄 (租用戶) 識別碼 
CLIENT_ID = '' # 應用程式 (用戶端) 識別碼
KEY = '' # 用戶端密碼
WORKSPACE_ID = '' # 工作區ID

credentials = ServicePrincipalCredentials(
    client_id = CLIENT_ID,
    secret = KEY,
    tenant = TENANT_ID,
    resource = "https://api.loganalytics.io"
)

client = loganalytics.log_analytics_data_client.LogAnalyticsDataClient(credentials, base_url=None)

workspace_id = WORKSPACE_ID
body = loganalytics.models.QueryBody(query = "ContainerLog | where TimeGenerated < ago(1m) | where TimeGenerated < ago(10m)") # 前十分鐘的 Container Log

query_results = client.query(workspace_id, body) # type: https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/loganalytics/azure-loganalytics/azure/loganalytics/models/query_results.py
table = query_results.tables[0] # https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/loganalytics/azure-loganalytics/azure/loganalytics/models/table.py
columns = table.columns
rows = table.rows # [][] of arbitrary data

print(columns) # VERY noisy
print(rows)
