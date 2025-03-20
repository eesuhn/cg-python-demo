# `cg-python-demo`

Demo playground for the [`cg-python`](https://github.com/eesuhn/cg-python) SDK.

## Getting Started

### Structure

```sh
.
├── Makefile
├── README.md
├── app
│   ├── __init__.py
│   ├── _constants.py
│   ├── main.py  # 👈 Main logic
│   └── utils.py
├── cg-python  # 👈 SDK
└── main.py
```

1. Fetch the `cg-python` SDK:

    ```bash
    make submodule
    ```

2. Install the SDK in project environment:

    ```bash
    make sdk
    ```

3. Set up API keys in `.env`:

    ```bash
    cp .env.example .env
    ```

    ```env
    CG_PRO_API_KEY=YOUR_PRO_API_KEY
    CG_DEMO_API_KEY=YOUR_DEMO_API_KEY
    ```

4. Run the demo in `app/main.py`:

    ```bash
    make run
    ```

## Usage

Full example in [`app/main.py`](./app/main.py).

### 1. Set the API client + Select the API method

```python
def __init__(self) -> None:
    self.api_client = self.set_pro()  # 👈 Set the API client
    # self.api_client = self.set_demo()
    self.run()

def run(self) -> None:
    # self.get_simple_supported_currencies()
    # self.get_networks_list()
    self.get_pools_megafilter()  # 👈 Uncomment to run
    pass
```

### 2. Setting Pro/Demo client

Choose between `'proKeyAuth'` or `'demoKeyAuth'` for the API key:

```python
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
```

### 3. Example — 🔥 Megafilter for Pools

```python
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
```
