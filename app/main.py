from coingecko_python.configuration import Configuration
from coingecko_python.api_client import ApiClient
from coingecko_python.exceptions import ApiException
from coingecko_python import (
    NetworksApi,
    SimpleApi,
    PoolsApi
)
from ._constants import (
    CG_PRO_API_KEY,
    CG_DEMO_API_KEY
)
from .utils import (
    print_json
)


class Main:
    def __init__(self) -> None:
        # api_sdk = self.set_demo()
        api_sdk = self.set_pro()
        with api_sdk as api_client:
            # self.get_simple_supported_currencies(api_client)
            self.get_networks_list(api_client)
            # self.get_pools_megafilter(api_client)
            pass

    def set_pro(self) -> ApiClient:
        """Set the API client with the PRO key"""
        configuration = Configuration(
            server_index=0,
        )
        configuration.api_key['proKeyAuth'] = f"{CG_PRO_API_KEY}"
        return ApiClient(configuration)

    def set_demo(self) -> ApiClient:
        """Set the API client with the DEMO key"""
        configuration = Configuration(
            server_index=1,
            # host="https://api.coingecko.com/api/v3"  # OR this way
        )
        configuration.api_key['demoKeyAuth'] = f"{CG_DEMO_API_KEY}"
        return ApiClient(configuration)

    def get_networks_list(self, api_client: ApiClient) -> None:
        """https://docs.coingecko.com/reference/networks-list"""
        api_instance = NetworksApi(api_client)
        try:
            api_response = api_instance.networks_list()
            print_json(api_response.to_dict())
        except ApiException as e:
            print("Exception when calling NetworksApi->networks_list: %s\n" % e)

    def get_simple_supported_currencies(self, api_client: ApiClient) -> None:
        """https://docs.coingecko.com/reference/simple-supported-currencies"""
        api_instance = SimpleApi(api_client)
        try:
            api_response = api_instance.simple_supported_currencies()
            print_json(api_response)
        except ApiException as e:
            print("Exception when calling SimpleApi->simple_supported_currencies: %s\n" % e)

    def get_pools_megafilter(self, api_client: ApiClient) -> None:
        """https://docs.coingecko.com/reference/pools-megafilter"""
        api_instance = PoolsApi(api_client)
        try:
            api_response = api_instance.pools_megafilter()
            print_json(api_response)
        except ApiException as e:
            print("Exception when calling PoolsApi->pools_megafilter: %s\n" % e)
