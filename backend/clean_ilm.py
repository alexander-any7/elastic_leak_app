from elasticsearch import Elasticsearch
import urllib3

# Sertifika uyarılarını kapat
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Elasticsearch bağlantısı
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elasticuser", "elasticuser_password"),
    verify_certs=False,
    request_timeout=100
)

# 1. ILM Policy sil
try:
    es.ilm.delete_lifecycle(name="leaks_policy")
    print("✅ ILM policy deleted: leaks_policy")
except Exception as e:
    print(f"⚠️ ILM policy could not be deleted: {e}")

# 2. Index Template sil
try:
    es.indices.delete_index_template(name="leaks_template")
    print("✅ Index template deleted: leaks_template")
except Exception as e:
    print(f"⚠️ Index template could not be deleted: {e}")

# 3. Alias ve index sil
try:
    es.indices.delete(index="leaks-000001")
    print("✅ Index deleted: leaks-000001")
except Exception as e:
    print(f"⚠️ Index could not be deleted: {e}")

# (Opsiyonel) Eğer başka leaks-* index'leri varsa onları da sil
try:
    indices = es.indices.get(index="leaks-*").keys()
    for index in indices:
        es.indices.delete(index=index)
        print(f"✅ Ek index deleted: {index}")
except Exception as e:
    print(f"⚠️ Ek leaks-* indexes could not be retrieved or deleted: {e}")
