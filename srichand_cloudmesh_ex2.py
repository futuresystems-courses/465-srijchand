import yaml
with open('/home/ubuntu/.cloudmesh/cloudmesh.yaml', 'r') as f:
        doc = yaml.load(f)
txt = doc['cloudmesh']['clouds']
print txt

