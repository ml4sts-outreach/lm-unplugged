# lm-unplugged
an introduction to language models, unplugged


## Fully local interactive:

```bash
# Set the port for our local Jupyter process
port="8898"

# Define environment variables that will be used by MyST
# We'll use the values of these variables in our Jupyter server as well.
export JUPYTER_BASE_URL="http://localhost:${port}"
export JUPYTER_TOKEN="lm-unplugged-tok"

# Start the Jupyter server re-using the variables above
jupyter server --IdentityProvider.token="${JUPYTER_TOKEN}" --ServerApp.token="${JUPYTER_TOKEN}" --ServerApp.port="${port}"  --ServerApp.allow_origin='http://localhost:3001' &
# Run the MyST build
# It will use the JUPYTER_* variables above to look for the server.
myst start --execute
```
