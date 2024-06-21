#!/usr/local/bin/python3
from dataclasses import dataclass
import sys
from arcaflow_plugin_sdk import plugin


@dataclass
class InputParams:
    name: str


@dataclass
class SuccessOutput:
    message: str


@plugin.step(
    id="hello-world",
    name="Hello world!",
    description="Says hello :)",
    outputs={"success": SuccessOutput},
)
def hello_world(params: InputParams):
    return "success", SuccessOutput(f"Hello, {params.name}")


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                hello_world,
            )
        )
    )
