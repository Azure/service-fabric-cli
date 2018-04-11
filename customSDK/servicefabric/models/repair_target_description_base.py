# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RepairTargetDescriptionBase(Model):
    """Describes the entities targeted by a repair action.
    This type supports the Service Fabric platform; it is not meant to be used
    directly from your code.
    .

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: NodeRepairTargetDescription

    :param kind: Constant filled by server.
    :type kind: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'Node': 'NodeRepairTargetDescription'}
    }

    def __init__(self):
        self.kind = None