# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Trainer Component Examples
==========================

Component definitions that run the example lightning_classy_vision app
in a single or distributed manner.

Prerequisites of running examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before executing examples, install torchx and dependencies necessary to run examples:

.. code:: bash

   pip install torchx
   git clone https://github.com/pytorch/torchx.git
   cd torchx
   pip install -r dev-requirements.txt

.. note::

     The working dir should be ``torchx`` to run the components.


"""

# Importing torchx api specifications

from typing import Optional, Dict, List

import torchx.specs.api as torchx
from torchx.specs import macros, named_resources, Resource
from torchx.version import TORCHX_IMAGE


# %%
# Trainer Component
# ###################
# Defines a single trainer component
#
# Use the following cmd to try out:
#
# .. code:: bash
#
#    torchx run --scheduler local_cwd \
#    ./torchx/examples/apps/lightning_classy_vision/component.py:trainer \
#    --output_path /tmp
#
# Single trainer component code:


def trainer(
    output_path: Optional[str] = None,
    image: str = TORCHX_IMAGE,
    data_path: Optional[str] = None,
    load_path: str = "",
    log_path: str = "/tmp/logs",
    resource: Optional[str] = None,
    env: Optional[Dict[str, str]] = None,
    skip_export: bool = False,
    epochs: int = 1,
    layers: Optional[List[int]] = None,
    learning_rate: Optional[float] = None,
    num_samples: int = 200,
) -> torchx.AppDef:
    """Runs the example lightning_classy_vision app.

    Args:
        output_path: output path for model checkpoints (e.g. file:///foo/bar)
        image: image to run (e.g. foobar:latest)
        load_path: path to load pretrained model from
        data_path: path to the data to load, if data_path is not provided,
            auto generated test data will be used
        log_path: path to save tensorboard logs to
        resource: the resources to use
        env: env variables for the app
        skip_export: disable model export
        epochs: number of epochs to run
        layers: the number of convolutional layers and their number of channels
        learning_rate: the learning rate to use for training
        num_samples: the number of images to run per batch, use 0 to run on all
    """
    env = env or {}
    args = [
        "-m",
        "torchx.examples.apps.lightning_classy_vision.train",
        "--load_path",
        load_path,
        "--log_path",
        log_path,
        "--epochs",
        str(epochs),
    ]
    if output_path:
        args += ["--output_path", output_path]
    if layers:
        args += ["--layers"] + [str(layer) for layer in layers]
    if learning_rate:
        args += ["--lr", str(learning_rate)]
    if num_samples and num_samples > 0:
        args += ["--num_samples", str(num_samples)]
    if data_path:
        args += ["--data_path", data_path]
    if skip_export:
        args.append("--skip_export")
    return torchx.AppDef(
        name="cv-trainer",
        roles=[
            torchx.Role(
                name="worker",
                entrypoint="python",
                args=args,
                env=env,
                image=image,
                resource=named_resources[resource]
                if resource
                else torchx.Resource(cpu=1, gpu=0, memMB=3000),
            )
        ],
    )


# %%
# Distributed Trainer Component
# ###############################
#


def trainer_dist(
    output_path: Optional[str] = None,
    image: str = TORCHX_IMAGE,
    data_path: Optional[str] = None,
    load_path: str = "",
    log_path: str = "/tmp/logs",
    resource: Optional[str] = None,
    env: Optional[Dict[str, str]] = None,
    skip_export: bool = False,
    epochs: int = 1,
    nnodes: int = 1,
    nproc_per_node: int = 1,
    rdzv_backend: str = "etcd",
    rdzv_endpoint: str = "etcd-server:2379",
) -> torchx.AppDef:
    """Runs the example lightning_classy_vision app.

    Args:
        output_path: output path for model checkpoints (e.g. file:///foo/bar)
        image: image to run (e.g. foobar:latest)
        load_path: path to load pretrained model from
        data_path: path to the data to load, if data_path is not provided,
            auto generated test data will be used
        log_path: path to save tensorboard logs to
        resource: the resources to use
        env: env variables for the app
        skip_export: disable model export
        epochs: number of epochs to run
        nnodes: number of nodes to run train on, default 1
        nproc_per_node: number of processes per node. Each process
            is assumed to use a separate GPU, default 1
        rdzv_backend: rendezvous backend to use, allowed values can be found at
            `repistry <https://github.com/pytorch/pytorch/blob/master/torch/distributed/elastic/rendezvous/registry.py>`_
            The default backend is ``etcd``
        rdzv_endpoint: Controller endpoint. In case of rdzv_backend is etcd, this is a etcd
            endpoint, in case of c10d, this is the endpoint of one of the hosts.
            The default endpoint is ``etcd-server:2379``
    """
    env = env or {}
    args = [
        "-m",
        "torch.distributed.run",
        "--rdzv_backend",
        rdzv_backend,
        "--rdzv_endpoint",
        rdzv_endpoint,
        "--rdzv_id",
        f"{macros.app_id}",
        "--nnodes",
        str(nnodes),
        "--nproc_per_node",
        str(nproc_per_node),
        "-m",
        "torchx.examples.apps.lightning_classy_vision.train",
        "--load_path",
        load_path,
        "--log_path",
        log_path,
        "--epochs",
        str(epochs),
    ]
    if output_path:
        args += ["--output_path", output_path]
    if data_path:
        args += ["--data_path", data_path]
    if skip_export:
        args.append("--skip_export")
    resource_def = (
        named_resources[resource]
        if resource
        else Resource(cpu=nnodes, gpu=0, memMB=3000)
    )
    return torchx.AppDef(
        name="cv-trainer",
        roles=[
            torchx.Role(
                name="worker",
                entrypoint="python",
                args=args,
                env=env,
                image=image,
                resource=resource_def,
                num_replicas=nnodes,
            )
        ],
    )


# %%
# Interpreting the Model
# #######################
# Defines a component that interprets the model
#
# Train a single trainer example: :ref:`examples_apps/lightning_classy_vision/component:Trainer Component`
# And use the following cmd to try out:
#
# .. code:: bash
#
#    torchx run --scheduler local_cwd \
#    ./torchx/examples/apps/lightning_classy_vision/component.py:interpret \
#    --output_path /tmp/aivanou/interpret  --load_path /tmp/$USER/last.ckpt


def interpret(
    load_path: str,
    output_path: str,
    data_path: Optional[str] = None,
    image: str = TORCHX_IMAGE,
    resource: Optional[str] = None,
) -> torchx.AppDef:
    """Runs the model interpretability app on the model outputted by the training
    component.

    Args:
        load_path: path to load pretrained model from
        output_path: output path for model checkpoints (e.g. file:///foo/bar)
        data_path: path to the data to load
        image: image to run (e.g. foobar:latest)
        resource: the resources to use
    """
    args = [
        "-m",
        "torchx.examples.apps.lightning_classy_vision.interpret",
        "--load_path",
        load_path,
        "--output_path",
        output_path,
    ]
    if data_path:
        args += [
            "--data_path",
            data_path,
        ]

    return torchx.AppDef(
        name="cv-interpret",
        roles=[
            torchx.Role(
                name="worker",
                entrypoint="python",
                args=args,
                image=image,
                resource=named_resources[resource]
                if resource
                else torchx.Resource(cpu=1, gpu=0, memMB=1024),
            )
        ],
    )
