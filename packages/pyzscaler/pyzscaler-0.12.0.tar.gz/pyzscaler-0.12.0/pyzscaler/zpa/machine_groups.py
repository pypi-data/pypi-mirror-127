from box import BoxList
from restfly.endpoint import APIEndpoint

from pyzscaler.utils import Iterator


class MachineGroupsAPI(APIEndpoint):
    def list_groups(self, **kwargs):
        """
        Returns a list of all configured machine groups.

        Returns:
            :obj:`list`: A list of all configured machine groups.

        Examples:
            >>> for machine_group in zpa.machine_groups.list_groups():
            ...    pprint(machine_group)

        """
        return BoxList(Iterator(self._api, "machineGroups", **kwargs))

    def get_group(self, group_id: str):
        """
        Returns information on the specified machine group.

        Args:
            group_id (str):
                The unique identifier for the machine group.

        Returns:
            :obj:`dict`: The resource record for the machine group.

        Examples:
            >>> pprint(zpa.machine_groups.get_group('2342342342344433'))

        """

        return self._get(f"machineGroups/{group_id}")
