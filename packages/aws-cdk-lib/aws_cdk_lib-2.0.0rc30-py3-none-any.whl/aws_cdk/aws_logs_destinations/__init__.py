'''
# CDK Construct Libray for AWS XXX

A short description here.
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
from ..aws_kinesis import IStream as _IStream_4e2457d2
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_logs import (
    ILogGroup as _ILogGroup_3c4fa718,
    ILogSubscriptionDestination as _ILogSubscriptionDestination_99a12804,
    LogSubscriptionDestinationConfig as _LogSubscriptionDestinationConfig_15877ced,
)


@jsii.implements(_ILogSubscriptionDestination_99a12804)
class KinesisDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs_destinations.KinesisDestination",
):
    '''(experimental) Use a Kinesis stream as the destination for a log subscription.

    :stability: experimental
    '''

    def __init__(self, stream: _IStream_4e2457d2) -> None:
        '''
        :param stream: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [stream])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: constructs.Construct,
        _source_log_group: _ILogGroup_3c4fa718,
    ) -> _LogSubscriptionDestinationConfig_15877ced:
        '''(experimental) Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param _source_log_group: -

        :stability: experimental
        '''
        return typing.cast(_LogSubscriptionDestinationConfig_15877ced, jsii.invoke(self, "bind", [scope, _source_log_group]))


@jsii.implements(_ILogSubscriptionDestination_99a12804)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs_destinations.LambdaDestination",
):
    '''(experimental) Use a Lambda Function as the destination for a log subscription.

    :stability: experimental
    '''

    def __init__(
        self,
        fn: _IFunction_6adb0ab8,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) LambdaDestinationOptions.

        :param fn: -
        :param add_permissions: (experimental) Whether or not to add Lambda Permissions. Default: true

        :stability: experimental
        '''
        options = LambdaDestinationOptions(add_permissions=add_permissions)

        jsii.create(self.__class__, self, [fn, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: constructs.Construct,
        log_group: _ILogGroup_3c4fa718,
    ) -> _LogSubscriptionDestinationConfig_15877ced:
        '''(experimental) Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param log_group: -

        :stability: experimental
        '''
        return typing.cast(_LogSubscriptionDestinationConfig_15877ced, jsii.invoke(self, "bind", [scope, log_group]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs_destinations.LambdaDestinationOptions",
    jsii_struct_bases=[],
    name_mapping={"add_permissions": "addPermissions"},
)
class LambdaDestinationOptions:
    def __init__(
        self,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options that may be provided to LambdaDestination.

        :param add_permissions: (experimental) Whether or not to add Lambda Permissions. Default: true

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if add_permissions is not None:
            self._values["add_permissions"] = add_permissions

    @builtins.property
    def add_permissions(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether or not to add Lambda Permissions.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("add_permissions")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KinesisDestination",
    "LambdaDestination",
    "LambdaDestinationOptions",
]

publication.publish()
