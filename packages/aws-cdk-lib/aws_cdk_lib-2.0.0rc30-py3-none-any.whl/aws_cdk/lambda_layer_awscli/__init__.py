'''
# AWS Lambda Layer with AWS CLI

This module exports a single class called `AwsCliLayer` which is a `lambda.Layer` that bundles the AWS CLI.

Usage:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
fn = lambda_.Function(...)
fn.add_layers(AwsCliLayer(stack, "AwsCliLayer"))
```

The CLI will be installed under `/opt/awscli/aws`.
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


class AwsCliLayer(
    _LayerVersion_9ca26241,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.lambda_layer_awscli.AwsCliLayer",
):
    '''(experimental) An AWS Lambda layer that includes the AWS CLI.

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
    "AwsCliLayer",
]

publication.publish()
