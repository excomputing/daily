
<br>

## Notes

**Interacting with Amazon Simple Storage Service**

```shell
aws s3 rm s3://{bucket.name}  --recursive
aws s3 rb s3://{bucket.name}
```

<br>

**Images & Containers**

Docker <span title="command line interface">CLI</span> [Reference](https://docs.docker.com/reference/cli/docker/):

* [Container Volumes](https://docs.docker.com/reference/cli/docker/volume/create/)

<br>

**Inbetween Windows & Windows Subsystem for Linux (WSL)**

Specifically, transferring documents between Windows and a WSL Linux Kernel

```shell
cp /mnt/v/../compose.yaml /home/../..
```

<br>

**Testing Locally**

The image's programs interact with Amazon services therefore an image container will require Amazon credentials. Hence, a 
local testing option is a compose.yaml; a `compose.yaml` of the form [compose.yaml.template](/compose.yaml.template), **explanatory notes 
upcoming**. Subsequently, within the directory hosting `compose.yaml`

```shell
docker pull ghcr.io/enqueter/daily:develop
docker compose up --detach
```

If any problems arise

```shell
docker compose logs --follow
```

Visit docker.docs.com for more about [`docker compose up`](https://docs.docker.com/reference/cli/docker/compose/up/) & 
[`docker compose logs`](https://docs.docker.com/reference/cli/docker/compose/logs/)


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
