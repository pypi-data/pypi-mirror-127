## Upload data to a fhir server
Using this library resources can be added to a fhir server as single resources, lists or as predefined 
bundles.


### Uploading a single resource

Uploading a single resource is done by calling the `add` function on a FHIR server.
The response contains the resource including the server defined id of the resource.  
The add function takes as argument either a dictionary containing the definition of a resource or a 
pydantic model object of the resource.

#### Pydantic model

```python
from fhir_kindling import FhirServer
from fhir.resources.patient import Patient

patient = Patient(
    name=[
        {
            "family": "Smith",
            "given": ["John"],
        },
    ],
    birthdate="1955-05-05"
)

fhir_server = FhirServer(api_address="http://fhir.example.com/R4")
response = fhir_server.add(resource=patient)
```

To upload an existing bundle to a FHIR server use the upload command of the cli, or the top level upload module


## Transferring data between FHIR servers


### CLI

View the configuration options for the upload command by executing `fhir_kindling upload --help`.
To upload a json bundle specify its path (or the path to a directory containing multiple bundles).
```terminal
fhir_kindling upload <path-to-bundle> [options]
```

#### Specifying the FHIR server and credentials
Select the server and authentication as command line arguments:

- `--url` specifies the base endpoint of the REST api of the FHIR server to upload to
- `-u`/`--username` username to use in Basicauth authentication for the server
- `-p`/`--password` password for Basicauth
- `-t`/`--token` token to be used as Bearer token for token based authentication (keycloak, OIDC)

If these are not present, the tool will look for authentication information under the environment variables:

- `FHIR_API_URL`
- `FHIR_USER`
- `FHIR_PW`
- `FHIR_TOKEN`

If the token option is set either via arguments or environment variables, the user and password option can not also
be set.


## API docs
Docs for interacting with the upload functionality programmatically.

::: fhir_kindling.cli.upload.upload_bundle
    rendering:
      heading_level: 3
      show_root_heading: True
      show_root_full_path: False

::: fhir_kindling.cli.upload.upload_resource
    rendering:
      heading_level: 3
      show_root_heading: True
      show_root_full_path: False






