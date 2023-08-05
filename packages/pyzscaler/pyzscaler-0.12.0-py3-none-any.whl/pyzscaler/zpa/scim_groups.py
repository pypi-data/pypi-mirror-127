from box import BoxList
from restfly.endpoint import APIEndpoint

from pyzscaler.utils import Iterator


class SCIMGroupsAPI(APIEndpoint):
    def list_groups(self, **kwargs):
        """
        Returns a list of all configured SCIM groups.

        Returns:
            :obj:`list`: A list of all configured SCIM groups.

        Examples:
            >>> for scim_group in zpa.scim_groups.list_groups():
            ...    pprint(scim_group)

        """
        return BoxList(Iterator(self._api, "scimgroup", **kwargs))

    def get_group(self, idp_id: str):
        """
        Returns information on the specified SCIM group.

        Args:
            idp_id (str):
                The unique identifier for the Idp corresponding to the SCIM group.

        Returns:
            :obj:`dict`: The resource record for the SCIM group.

        Examples:
            >>> pprint(zpa.scim_groups.get_group('2342342342344433'))

        """

        return self._get(f"scimgroup/idpId/{idp_id}")
