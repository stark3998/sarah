from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'florassist' # Must be replaced by your <storage_account_name>
    account_key = 'wv4s5m3Ji9+bd0y3gb8wekwG3kwZ+BOzuaFx0adWqDjcaFy4pljq2OcQOOiZpGy0oJ52ffhgcTe7od4b1QStlA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'florassist' # Must be replaced by your storage_account_name
    account_key = 'wv4s5m3Ji9+bd0y3gb8wekwG3kwZ+BOzuaFx0adWqDjcaFy4pljq2OcQOOiZpGy0oJ52ffhgcTe7od4b1QStlA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None