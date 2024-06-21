FROM quay.io/arcalot/arcaflow-plugin-baseimage-python-osbase

ADD plugin.py /
RUN python -m pip install arcaflow_plugin_sdk

ENTRYPOINT ["python", "/plugin.py"]
CMD []