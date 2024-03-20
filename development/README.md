
<br>

### Notes

**Testing Locally**

The image's programs interact with Amazon services therefore an image container will require Amazon credentials. Hence, a 
local testing option is a compose.yaml; a `compose.yaml` of the form [compose.yaml.template](/compose.yaml.template), **explanatory notes 
upcoming**. Subsequently, within the directory hosting `compose.yaml`

```shell
docker pull ghcr.io/enqueter/daily:develop
docker compose up --detach
```

Logs

```shell
docker compose logs --follow
```

Visit [docker's reference pages](https://docs.docker.com/reference/) for more about [`docker compose up`](https://docs.docker.com/reference/cli/docker/compose/up/) & 
[`docker compose logs`](https://docs.docker.com/reference/cli/docker/compose/logs/)

<br>

**Testing via Amazon EC2 (Elastic Compute Cloud)**

If an EC2 machine is launched with the appropriate instance profile policies for interacting with relevant Amazon services, 
then testing is straightforward.

```shell
docker pull ghcr.io/enqueter/daily:develop
docker run ghcr.io/enqueter/daily:develop
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
