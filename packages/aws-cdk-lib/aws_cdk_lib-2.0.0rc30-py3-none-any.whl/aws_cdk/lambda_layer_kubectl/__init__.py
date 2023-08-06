'''
# AWS Lambda Layer with kubectl (and helm)

This module exports a single class called `KubectlLayer` which is a `lambda.Layer` that bundles the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/kubectl/) and the [`helm`](https://helm.sh/) command line.

> * Helm Version: 3.5.4
> * Kubectl Version: 1.20.0

Usage:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
fn = lambda_.Function(...)
fn.add_layers(KubectlLayer(stack, "KubectlLayer"))
```

`kubectl` will be installed under `/opt/kubectl/kubectl`, and `helm` will be installed under `/opt/helm/helm`.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from ..aws_lambda import LayerVersion as _LayerVersion_9ca26241


class KubectlLayer(
    _LayerVersion_9ca26241,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.lambda_layer_kubectl.KubectlLayer",
):
    '''(experimental) An AWS Lambda layer that includes ``kubectl`` and ``helm``.

    :stability: experimental
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [scope, id])


__all__ = [
    "KubectlLayer",
]

publication.publish()
