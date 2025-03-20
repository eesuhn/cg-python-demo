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
        self.api_client = self.set_pro()
        # self.api_client = self.set_demo()
        self.run()

    def run(self) -> None:
        # self.get_simple_supported_currencies()
        # self.get_networks_list()
        self.get_pools_megafilter()
        pass

    def set_pro(self) -> ApiClient:
        """
        Set the API client with the PRO key and host
        """
        configuration = Configuration(
            server_index=0,  # 👈 Pro API host
            # host="https://pro-api.coingecko.com/api/v3"  # OR this way
        )
        configuration.api_key['proKeyAuth'] = f"{CG_PRO_API_KEY}"  # 👈 Pro API key
        return ApiClient(configuration)

    def set_demo(self) -> ApiClient:
        """
        Set the API client with the DEMO key and host
        """
        configuration = Configuration(
            server_index=1,  # 👈 Demo API host
            # host="https://api.coingecko.com/api/v3"  # OR this way
        )
        configuration.api_key['demoKeyAuth'] = f"{CG_DEMO_API_KEY}"  # 👈 Demo API key
        return ApiClient(configuration)

    def get_networks_list(self) -> None:
        """
        https://docs.coingecko.com/reference/networks-list
        """
        api_instance = NetworksApi(self.api_client)
        try:
            api_response = api_instance.networks_list()
            print_json(api_response.to_dict())
        except ApiException as e:
            print("Exception when calling NetworksApi->networks_list: %s\n" % e)

    def get_simple_supported_currencies(self) -> None:
        """
        https://docs.coingecko.com/reference/simple-supported-currencies
        """
        api_instance = SimpleApi(self.api_client)
        try:
            api_response = api_instance.simple_supported_currencies()
            print_json(api_response)
        except ApiException as e:
            print("Exception when calling SimpleApi->simple_supported_currencies: %s\n" % e)

    def get_pools_megafilter(self) -> None:
        """
        https://docs.coingecko.com/reference/pools-megafilter
        """
        api_instance = PoolsApi(self.api_client)
        try:
            api_response = api_instance.pools_megafilter()
            print_json(api_response.to_dict())
        except ApiException as e:
            print("Exception when calling PoolsApi->pools_megafilter: %s\n" % e)
