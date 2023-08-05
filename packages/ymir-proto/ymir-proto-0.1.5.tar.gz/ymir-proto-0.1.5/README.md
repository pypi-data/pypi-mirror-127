# YMIR Protocols

## install

```bash
pip install ymir-proto
```

## usage

```python
# protobufs
from ymir.protos import mir_controller_service_pb2
from ymir.protos import mir_controller_service_pb2_grpc
from ymir.protos import mir_common_pb2
from ymir.protos import mir_entities_pb2

# task_id
from ymir.ids import task_id

# class_ids
from ymir.ids import class_ids
```


## requirement

```bash
pip install grpcio-tools
```

## develop

1. modify pbs in ./protos  
2. `bash update_proto_py.sh`
3. install locally: `pip install .`
