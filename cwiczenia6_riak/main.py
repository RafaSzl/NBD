from riak import RiakClient

client = RiakClient(pb_port=8087)
bucket = client.bucket('s24214')

new_row = {
    'name': 'Izabela',
    'surname': 'Lecka',
    'salary': 99,
    'year': 1000
}
key = 'test_key'
bucket.new(key, data=new_row).store()

doc = bucket.get(key)
print(f'New document:\n{doc.data}\n\n')

doc.data["salary"] = 100
doc.store()

doc_modified = bucket.get(key)
print(f'Modified document:\n{doc_modified.data}\n\n')

doc_modified.delete()

doc_deleted = bucket.get(key)
print(f'Deleted document:\n{doc_deleted.data}')