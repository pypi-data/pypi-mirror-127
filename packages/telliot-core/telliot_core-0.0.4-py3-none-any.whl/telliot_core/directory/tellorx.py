import json
from pathlib import Path

from telliot_core.directory._tellorx.temp_contracts import rinkeby_tellor_master
from telliot_core.directory._tellorx.temp_contracts import rinkeby_tellor_oracle
from telliot_core.directory.base import ContractDirectory
from telliot_core.directory.base import ContractInfo

__all__ = ["tellor_directory"]

_tellor_address_mainnet = {
    "master": "0x88dF592F8eb5D7Bd38bFeF7dEb0fBc02cf3778a0",
    "controller": "",
    "oracle": "",
    "governance": "",
    "treasury": "",
}

_tellor_address_rinkeby = {
    "master": "0x88dF592F8eb5D7Bd38bFeF7dEb0fBc02cf3778a0",
    "controller": "0x0f2B0a8fa0f60459f51E452273C879eb32555e91",
    "oracle": "0x18431fd88adF138e8b979A7246eb58EA7126ea16",
    "governance": "0xA64Bb0078eB80c97484f3f09Adb47b9B73CBcA00",
    "treasury": "0x2dB91443f2b562B8b2B2e8E4fC0A3EDD6c195147",
}

# Read contract ABIs from json files
_abi_folder = Path(__file__).resolve().parent / "_tellorx"
_abi_dict = {}
for name in ["master", "controller", "oracle", "governance", "treasury"]:
    with open(_abi_folder / f"{name}_abi.json", "r") as f:
        _abi_dict[name] = json.load(f)

# Create default tellor directory
tellor_directory = ContractDirectory()

for name in ["master", "controller", "oracle", "governance", "treasury"]:
    # Add maininet contract info entry
    tellor_directory.add_contract(
        ContractInfo(
            chain_id=1,
            org="tellor",
            name=name,
            address=_tellor_address_mainnet[name],
            abi=_abi_dict[name],
        )
    )

    # Add rinkeby contract info entry
    tellor_directory.add_contract(
        ContractInfo(
            chain_id=4,
            org="tellor",
            name=name,
            address=_tellor_address_rinkeby[name],
            abi=_abi_dict[name],
        )
    )


# TEMPORARY OVERRIDE ADDRESS and ABI WITH TEST VALUES

_tellor_address_rinkeby_temp = {
    "master": "0x657b95c228A5de81cdc3F85be7954072c08A6042",
    "oracle": "0x07b521108788C6fD79F471D603A2594576D47477",
}

tellor_master_rinkeby = tellor_directory.find(chain_id=4, name="master")[0]
tellor_master_rinkeby.address = _tellor_address_rinkeby_temp["master"]
tellor_master_rinkeby.abi = rinkeby_tellor_master

tellor_oracle_rinkeby = tellor_directory.find(chain_id=4, name="oracle")[0]
tellor_oracle_rinkeby.address = _tellor_address_rinkeby_temp["oracle"]
tellor_oracle_rinkeby.abi = rinkeby_tellor_oracle
