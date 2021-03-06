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


class PerformanceTierProperties(Model):
    """Performance tier properties.

    :param id: ID of the performance tier.
    :type id: str
    :param max_backup_retention_days: Maximum Backup retention in days for the
     performance tier edition
    :type max_backup_retention_days: int
    :param min_backup_retention_days: Minimum Backup retention in days for the
     performance tier edition
    :type min_backup_retention_days: int
    :param max_storage_mb: Max storage allowed for a server.
    :type max_storage_mb: int
    :param min_storage_mb: Max storage allowed for a server.
    :type min_storage_mb: int
    :param service_level_objectives: Service level objectives associated with
     the performance tier
    :type service_level_objectives:
     list[~azure.mgmt.rdbms.postgresql.models.PerformanceTierServiceLevelObjectives]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'max_backup_retention_days': {'key': 'maxBackupRetentionDays', 'type': 'int'},
        'min_backup_retention_days': {'key': 'minBackupRetentionDays', 'type': 'int'},
        'max_storage_mb': {'key': 'maxStorageMB', 'type': 'int'},
        'min_storage_mb': {'key': 'minStorageMB', 'type': 'int'},
        'service_level_objectives': {'key': 'serviceLevelObjectives', 'type': '[PerformanceTierServiceLevelObjectives]'},
    }

    def __init__(self, id=None, max_backup_retention_days=None, min_backup_retention_days=None, max_storage_mb=None, min_storage_mb=None, service_level_objectives=None):
        super(PerformanceTierProperties, self).__init__()
        self.id = id
        self.max_backup_retention_days = max_backup_retention_days
        self.min_backup_retention_days = min_backup_retention_days
        self.max_storage_mb = max_storage_mb
        self.min_storage_mb = min_storage_mb
        self.service_level_objectives = service_level_objectives
